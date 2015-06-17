import ROOT
import pickle 
import copy, os, sys
ROOT.gROOT.LoadMacro("../../HEPHYPythonTools/scripts/root/tdrstyle.C")
ROOT.setTDRStyle()

from Workspace.HEPHYPythonTools.helpers import *
from Workspace.HEPHYPythonTools.xsec import *
from Workspace.RA4Analysis.helpers import *
from Workspace.RA4Analysis.cmgTuples_v1_PHYS14V3 import *
from draw_helpers import *
from math import *
from localInfo import username
from LpTemplateFit import LpTemplateFit

preprefix = 'QCDestimation'
wwwDir = '/afs/hephy.at/user/d/dhandl/www/pngCMG2/hard/Phys14V3/'+preprefix+'/'
presel = 'dPhi_singleElectronic_'

if not os.path.exists(wwwDir):
  os.makedirs(wwwDir)

htreg = [(500,-1)]#, (750,1000)]
streg = [(200,-1)]#, (350,450), (450,-1)]
njreg = [(3,4)]#, (8,-1)]
btreg = [(0,0)]
dPhiBinning = [0,0.5,1.0,1.5,2.0,2.5,3.0,pi]

#small = True
small = False
#doFit = True
doFit = False

eleVarList = ['pt', 'eta', 'phi', 'pdgId', 'miniRelIso', 'convVeto', 'sip3d', 'mvaIdPhys14', 'charge', 'lostHits']
eleFromW = ['pt', 'eta', 'phi', 'pdgId', 'motherId', 'grandmotherId', 'charge', 'sourceId']

def getMatch(genLep,recoLep):
  return ( (genLep['charge']==recoLep['charge']) and deltaR(genLep,recoLep)<0.1 and (abs(genLep['pt']-recoLep['pt'])/genLep['pt'])<0.5)

target_lumi = 3000 #pb-1
def getWeight(sample,nEvents,target_lumi):
  weight = xsec[sample['dbsName']] * target_lumi/nEvents
  return weight

def antiSel(e):
  if abs(e['eta'])<0.8:
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.4 and e['mvaIdPhys14']>=0.35 and e['mvaIdPhys14']<0.73)
  if (abs(e['eta'])>=0.8 and abs(e['eta'])<1.4):
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.4 and e['mvaIdPhys14']>=0.20 and e['mvaIdPhys14']<0.57)
  if (abs(e['eta'])>=1.4 and abs(e['eta'])<2.4):
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.4 and e['mvaIdPhys14']>=(-0.52) and e['mvaIdPhys14']<0.05)
  return False

def sel(e):
  if abs(e['eta'])<0.8:
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.1 and e['convVeto']==1 and e['sip3d']<4.0 and e['lostHits']==0 and e['mvaIdPhys14']>=0.73)
  if (abs(e['eta'])>=0.8 and abs(e['eta'])<1.4):
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.1 and e['convVeto']==1 and e['sip3d']<4.0 and e['lostHits']==0 and e['mvaIdPhys14']>=0.57)
  if (abs(e['eta'])>=1.4 and abs(e['eta'])<2.4):
    return (e['pt']>=25 and abs(e['pdgId'])==11 and e['miniRelIso']<0.1 and e['convVeto']==1 and e['sip3d']<4.0 and e['lostHits']==0 and e['mvaIdPhys14']>=0.05)
  return False

def getDPhi(met,metPhi,e):
#  met = c.GetLeaf('met_pt').GetValue()
#  metPhi = c.GetLeaf('met_phi').GetValue()
  
  dPhi = acos((e['pt']+met*cos(e['phi']-metPhi))/sqrt(e['pt']**2+met**2+2*met*e['pt']*cos(e['phi']-metPhi)))
  return dPhi

Bkg = [#{'name':'QCD_HT_100To250_PU20bx25', 'sample':QCD_HT_100To250_PU20bx25, 'legendName':'QCD HT100-250', 'color':ROOT.kCyan+3},
       {'name':'QCD_HT_250To500_PU20bx25', 'sample':QCD_HT_250To500_PU20bx25, 'legendName':'QCD HT250-500', 'color':ROOT.kCyan, 'merge':'QCD'},
       {'name':'QCD_HT_500To1000_PU20bx25', 'sample':QCD_HT_500To1000_PU20bx25, 'legendName':'QCD HT500-1000', 'color':ROOT.kCyan-3, 'merge':'QCD'},
       {'name':'QCD_HT_1000ToInf_PU20bx25', 'sample':QCD_HT_1000ToInf_PU20bx25, 'legendName':'QCD HT1000-Inf', 'color':ROOT.kCyan-7, 'merge':'QCD'},
       {'name':'TBarToLeptons_sChannel_PU20bx25', 'sample':TBarToLeptons_sChannel_PU20bx25, 'legendName':'TBarToLep sCh', 'color':ROOT.kViolet, 'merge':'EWK'},
       {'name':'TBarToLeptons_tChannel_PU20bx25', 'sample':TBarToLeptons_tChannel_PU20bx25, 'legendName':'TBarToLep tCh', 'color':ROOT.kViolet-3, 'merge':'EWK'},
       {'name':'TToLeptons_sChannel_PU20bx25', 'sample':TToLeptons_sChannel_PU20bx25, 'legendName':'TToLep sCh', 'color':ROOT.kViolet-5, 'merge':'EWK'},
       {'name':'TToLeptons_tChannel_PU20bx25', 'sample':TToLeptons_tChannel_PU20bx25, 'legendName':'TToLep tCh', 'color':ROOT.kViolet-7, 'merge':'EWK'},
       {'name':'T_tWChannel_PU20bx25', 'sample':T_tWChannel_PU20bx25, 'legendName':'TtW', 'color':ROOT.kViolet+1, 'merge':'EWK'},
       {'name':'TBar_tWChannel_PU20bx25', 'sample':TBar_tWChannel_PU20bx25, 'legendName':'TBartW', 'color':ROOT.kViolet+6, 'merge':'EWK'},
       {'name':'ttWJets_PU20bx25', 'sample':ttWJets_PU20bx25, 'legendName':'tt+W', 'color':ROOT.kOrange, 'merge':'EWK'},
       {'name':'ttZJets_PU20bx25', 'sample':ttZJets_PU20bx25, 'legendName':'tt+Z', 'color':ROOT.kOrange+7, 'merge':'EWK'},
       {'name':'ttH_PU20bx25', 'sample':ttH_PU20bx25, 'legendName':'tt+H', 'color':ROOT.kOrange+4, 'merge':'EWK'},
       {'name':'DYJetsToLL_M50_HT100to200_PU20bx25', 'sample':DYJetsToLL_M50_HT100to200_PU20bx25, 'legendName':'DY HT100-200', 'color':ROOT.kRed, 'merge':'EWK'},
       {'name':'DYJetsToLL_M50_HT200to400_PU20bx25', 'sample':DYJetsToLL_M50_HT200to400_PU20bx25, 'legendName':'DY HT200-400', 'color':ROOT.kRed+2, 'merge':'EWK'},
       {'name':'DYJetsToLL_M50_HT400to600_PU20bx25', 'sample':DYJetsToLL_M50_HT400to600_PU20bx25, 'legendName':'DY HT400-600', 'color':ROOT.kRed-7, 'merge':'EWK'},
       {'name':'DYJetsToLL_M50_HT600toInf_PU20bx25', 'sample':DYJetsToLL_M50_HT600toInf_PU20bx25, 'legendName':'DY HT600-Inf', 'color':ROOT.kRed-8, 'merge':'EWK'},
       {'name':'WJetsToLNu_HT100to200_PU20bx25', 'sample':WJetsToLNu_HT100to200_PU20bx25, 'legendName':'W HT100-200', 'color':ROOT.kGreen+3, 'merge':'EWK'},
       {'name':'WJetsToLNu_HT200to400_PU20bx25', 'sample':WJetsToLNu_HT200to400_PU20bx25, 'legendName':'W HT200-400', 'color':ROOT.kGreen, 'merge':'EWK'},
       {'name':'WJetsToLNu_HT400to600_PU20bx25', 'sample':WJetsToLNu_HT400to600_PU20bx25, 'legendName':'W HT400-600', 'color':ROOT.kGreen-3, 'merge':'EWK'},
       {'name':'WJetsToLNu_HT600toInf_PU20bx25', 'sample':WJetsToLNu_HT600toInf_PU20bx25, 'legendName':'W HT600-Inf', 'color':ROOT.kGreen-7, 'merge':'EWK'},
       {'name':'ttJets_PU20bx25', 'sample':ttJets_PU20bx25, 'legendName':'ttJets', 'color':ROOT.kRed, 'merge':'EWK'},# 'prompt':False},
]

maxN=5 if small else -1

for sample in Bkg:
  sample['chunks'], sample['nEvents'] = getChunks(sample['sample'],treeName='treeProducerSusySingleLepton', maxN=maxN)
  sample['chain'] = ROOT.TChain('tree')
  for chunk in sample['chunks']:
    sample['chain'].Add(chunk['file'])

  sample['weight'] = getWeight(sample['sample'], sample['nEvents'], target_lumi)

histos = {}
bins = {}
for htb in htreg:
  bins[htb] = {}
  for stb in streg:
    bins[htb][stb] = {}
    for srNJet in njreg:
      bins[htb][stb][srNJet] = {}
      for btb in btreg:
        print 'Binning => ht: ',htb,'st: ',stb,'NJet: ',srNJet
        SRname = nameAndCut(stb, htb, srNJet, btb=btb, presel="(1)", charge="", btagVar = 'nBJetMediumCSV30')[0]#use this function only for the name string!!!
        #cut only includes very loose lepton selection, HT cut, NJet cut, Btagging and subleading JetPt>=80!!! St cut applied in the Event Loop!!!
#        cut = '(Sum$(abs(LepGood_pdgId)==11&&abs(LepGood_dxy)<=0.05&&abs(LepGood_dz)<=0.1)+Sum$(abs(LepOther_pdgId)==11&&abs(LepOther_dxy)<=0.05&&abs(LepOther_dz)<=0.1)>=1)&&'+htCut(htb, minPt=30, maxEta=2.4, njCorr=0.)+'&&'+ nBTagCut(btb, minPt=30, maxEta=2.4, minCSVTag=0.814)+'&&'+nJetCut(srNJet, minPt=30, maxEta=2.4)+'&&'+nJetCut(2, minPt=80, maxEta=2.4)
        cut = '(Sum$(abs(LepGood_pdgId)==11&&LepGood_pt>10)>=1)&&'+htCut(htb, minPt=30, maxEta=2.4, njCorr=0.)+'&&'+ nBTagCut(btb, minPt=30, maxEta=2.4, minCSVTag=0.814)+'&&'+nJetCut(srNJet, minPt=30, maxEta=2.4)+'&&'+nJetCut(2, minPt=80, maxEta=2.4)

        histos['merged_QCD']={}
        histos['merged_EWK']={}
        histos['merged_QCD']['antiSelection']=ROOT.TH1F('merged_QCD_antiSelection','merged_QCD_antiSelection',len(dPhiBinning)-1, array('d', dPhiBinning))
        histos['merged_QCD']['Selection']=ROOT.TH1F('merged_QCD_Selection','merged_QCD_Selection',len(dPhiBinning)-1, array('d', dPhiBinning))
        histos['merged_EWK']['antiSelection']=ROOT.TH1F('merged_EWK_antiSelection','merged_EWK_antiSelection',len(dPhiBinning)-1, array('d', dPhiBinning))
        histos['merged_EWK']['Selection']=ROOT.TH1F('merged_EWK_Selection','merged_EWK_Selection',len(dPhiBinning)-1, array('d', dPhiBinning))
        
        
        for sample in Bkg:
          histos[sample['name']] = {}
          histos[sample['name']]['antiSelection'] = ROOT.TH1F(sample['name']+'_antiSelection', sample['name']+'_antiSelection',len(dPhiBinning)-1, array('d', dPhiBinning))
          histos[sample['name']]['Selection'] = ROOT.TH1F(sample['name']+'_Selection', sample['name']+'_Selection',len(dPhiBinning)-1, array('d', dPhiBinning))
        
          #Get the event list 'eList' which has all the events satisfying the cut
          sample["chain"].Draw(">>eList",cut)
          elist = ROOT.gDirectory.Get("eList")
          number_events = elist.GetN()
          print "Sample ",sample['name'],": Will loop over", number_events,"events"
        
          #Event Loop
          for i in range(number_events):
            if i%10000==0:
              print "At %i of %i for sample %s"%(i,number_events,sample['name'])
            sample['chain'].GetEntry(elist.GetEntry(i))
        
            eles = [getObjDict(sample['chain'], 'LepGood_', eleVarList, j) for j in range(int(sample['chain'].GetLeaf('nLepGood').GetValue()))]
#                 + [getObjDict(sample['chain'], 'LepOther_', eleVarList, j) for j in range(int(sample['chain'].GetLeaf('nLepOther').GetValue()))]
        
            genEle = [getObjDict(sample['chain'], 'genLep_', eleFromW, j) for j in range(int(sample['chain'].GetLeaf('ngenLep').GetValue()))] 
        
            met=sample['chain'].GetLeaf('met_pt').GetValue()
            metPhi=sample['chain'].GetLeaf('met_phi').GetValue()
        
            eles = filter(lambda e:abs(e['pdgId'])==11, eles) 
            eles = filter(lambda e:e['pt']>=25, eles) 
            eles = filter(lambda e:e['miniRelIso']<0.4, eles) #require relIso
            eles = filter(lambda e:abs(e['eta'])<2.4, eles) 
        
            eles = filter(lambda e:(e['pt']+met)>=stb[0], eles) 

            if stb[1]>0:
              eles = filter(lambda e:(e['pt']+met)<stb[1], eles)

            for e in eles:
              e["antiSel"] =  antiSel(e) 
              e["sel"] =  sel(e) 

            elesSelected = filter(lambda e:e['sel'],eles)
            elesAntiSelected = filter(lambda e:e['antiSel'],eles)
            nElesSelected = len(elesSelected)
            nElesAntiSelected = len(elesAntiSelected)

            if not nElesSelected+nElesAntiSelected==1:continue
            #print "nElesSelected %i nElesAntiSelected %i"%(nElesSelected,nElesAntiSelected)
            if nElesSelected==1:
              recoEle = elesSelected[0]
              isSelected = True 
            else:
              recoEle = elesAntiSelected[0]
              isSelected = False 

            #gen Electrons        
            genEle = filter(lambda e:abs(e['pdgId'])==11, genEle)
            genEle = filter(lambda e:e['pt']>=10, genEle)

#            if len(eles)>1:
#        #      print len(eles), len(genEle)
#              continue

            if len(eles)==0:print "Should never happen"
 
#            if sample.has_key('prompt'):
#              if sample['prompt']:
#                for reco in eles:
#                  hasMatch=False
#                  for gen in genEle:
#                    if getMatch(gen,reco):
#                      if reco["antiSel"]:
#                        antiVal = getDPhi(met,metPhi,reco) 
#                        histos[sample['name']]['antiSelection'].Fill(antiVal,sample['weight'])
#                      if sel(reco):
#                        selVal = getDPhi(met,metPhi,reco)
#                        histos[sample['name']]['Selection'].Fill(selVal,sample['weight'])
#                    hasMatch=True
#        #          if not hasMatch:
#        #            if antiSel(reco):
#        #              antiVal = getDPhi(sample['chain'],reco)
#        #              histos[sample['name']]['antiSelection'].Fill(antiVal,sample['weight'])
#        #            elif Sel(reco):
#        #              selVal = getDPhi(sample['chain'],reco)
#        #              histos[sample['name']]['Selection'].Fill(selVal,sample['weight'])  
#        
#            else:
        #      print len(eles)
#            for reco in eles:
            lp = getDPhi(met,metPhi,recoEle)
            if isSelected:
              histos[sample['name']]['Selection'].Fill(lp,sample['weight'])
            else: 
              histos[sample['name']]['antiSelection'].Fill(lp,sample['weight'])
        
          del elist 
        
        canv = ROOT.TCanvas('canv','canv',600,600)
        canv.SetLogy()
        l = ROOT.TLegend(0.65,0.75,0.95,0.95)
        l.SetFillColor(0)
        l.SetBorderSize(1)
        l.SetShadowColor(ROOT.kWhite)
        
        text = ROOT.TLatex()
        text.SetNDC()
        text.SetTextSize(0.045)
        text.SetTextAlign(11)
        
        first = True
        antiMax=0
        selMax=0
        for sample in Bkg:
          histos[sample['name']]['antiSelection'].SetLineColor(sample['color'])
          histos[sample['name']]['antiSelection'].SetLineStyle(ROOT.kDashed)
          histos[sample['name']]['antiSelection'].SetLineWidth(2)
          histos[sample['name']]['antiSelection'].GetYaxis().SetTitle('# of Events')
          histos[sample['name']]['antiSelection'].GetXaxis().SetTitle('#Delta#Phi(W,l)')
          histos[sample['name']]['Selection'].SetLineColor(sample['color'])
          histos[sample['name']]['Selection'].SetLineWidth(2)
          histos[sample['name']]['Selection'].GetYaxis().SetTitle('# of Events')
          histos[sample['name']]['Selection'].GetXaxis().SetTitle('#Delta#Phi(W,l)')
          l.AddEntry(histos[sample['name']]['antiSelection'], sample['legendName']+' anti-selected')
          l.AddEntry(histos[sample['name']]['Selection'], sample['legendName']+' selected')
        
          if sample['merge']=='QCD':
            histos['merged_QCD']['antiSelection'].Add(histos[sample['name']]['antiSelection'])
            histos['merged_QCD']['Selection'].Add(histos[sample['name']]['Selection'])
        
          elif sample['merge']=='EWK':
            histos['merged_EWK']['antiSelection'].Add(histos[sample['name']]['antiSelection'])
            histos['merged_EWK']['Selection'].Add(histos[sample['name']]['Selection'])
        
          if first:
            histos[sample['name']]['antiSelection'].Draw()
            histos[sample['name']]['Selection'].Draw('same')
          else:
            histos[sample['name']]['antiSelection'].Draw('same')
            histos[sample['name']]['Selection'].Draw('same')
          first = False
        
          if histos[sample['name']]['antiSelection'].GetMaximum() > antiMax:
            antiMax = histos[sample['name']]['antiSelection'].GetMaximum()
          if histos[sample['name']]['Selection'].GetMaximum() > selMax:
            selMax = histos[sample['name']]['Selection'].GetMaximum()
        
        for sample in Bkg:
          histos[sample['name']]['antiSelection'].SetMaximum(1.5*antiMax)
          histos[sample['name']]['antiSelection'].SetMinimum(0.01)
          histos[sample['name']]['Selection'].SetMaximum(1.5*selMax)
          histos[sample['name']]['Selection'].SetMinimum(0.01)
        
        l.Draw() 
        text.DrawLatex(0.15,.96,"CMS Simulation")
        text.DrawLatex(0.65,0.96,"L="+str(target_lumi/1000)+" fb^{-1} (13 TeV)")
        
        canv.cd()
        canv.Print(wwwDir+presel+SRname+'_subBkg.png')
        canv.Print(wwwDir+presel+SRname+'_subBkg.root')
        canv.Print(wwwDir+presel+SRname+'_subBkg.pdf')
        
        mergeCanv = ROOT.TCanvas('merged Canv','merged Canv',600,600)
        mergeCanv.SetLogy()
        leg = ROOT.TLegend(0.65,0.75,0.95,0.95)
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetShadowColor(ROOT.kWhite)
        
        for hist in [histos['merged_QCD']['antiSelection'],histos['merged_QCD']['Selection'],histos['merged_EWK']['antiSelection'],histos['merged_EWK']['Selection']]:
          hist.SetStats(0)
          hist.GetYaxis().SetTitle('# of Events')
          hist.GetXaxis().SetTitle('#Delta#Phi(W,l)')
          hist.SetLineWidth(2)
       
#        NdataSel =  histos['merged_QCD']['Selection'].Integral() +  histos['merged_EWK']['Selection'].Integral() 
#        NdataAntiSel =  histos['merged_QCD']['antiSelection'].Integral() +  histos['merged_EWK']['antiSelection'].Integral() 
#        bins[htb][stb][srNJet][btb] = {'NdataSel':NdataSel, 'NdataAntiSel':NdataAntiSel}
  
        #do the template fit:
#        if doFit:
#          LpTemplates = {'EWKantiSel':histos['merged_EWK']['antiSelection'], 'EWKsel':histos['merged_EWK']['Selection'], 'QCDantiSel':histos['merged_QCD']['antiSelection'], 'QCDsel':histos['merged_QCD']['Selection']}
#          fit_QCD = LpTemplateFit(LpTemplates, prefix=presel+SRname, printDir='/afs/hephy.at/user/'+username[0]+'/'+username+'/www/pngCMG2/templateFit_Phys14V3/QCDestimation')
#          bins[htb][stb][srNJet][btb].update(fit_QCD)
     
        mergeCanv.cd() 
#        if histos['merged_QCD']['antiSelection'].Integral()>0:
#          histos['merged_QCD']['antiSelection'].Scale(1./histos['merged_QCD']['antiSelection'].Integral())
        histos['merged_QCD']['antiSelection'].SetLineColor(ROOT.kRed)
        histos['merged_QCD']['antiSelection'].SetLineStyle(ROOT.kDashed)
#        histos['merged_QCD']['antiSelection'].SetMaximum(1)
        histos['merged_QCD']['antiSelection'].SetMinimum(0.01)
        leg.AddEntry(histos['merged_QCD']['antiSelection'],'QCD anti-selected','l')
 
#        if histos['merged_QCD']['Selection'].Integral()>0:
#          histos['merged_QCD']['Selection'].Scale(1./histos['merged_QCD']['Selection'].Integral())      
        histos['merged_QCD']['Selection'].SetLineColor(ROOT.kRed)
#        histos['merged_QCD']['Selection'].SetMaximum(1)
        histos['merged_QCD']['Selection'].SetMinimum(0.01)
        leg.AddEntry(histos['merged_QCD']['Selection'],'QCD selected','l')
 
#        if histos['merged_EWK']['antiSelection'].Integral()>0:
#          histos['merged_EWK']['antiSelection'].Scale(1./histos['merged_EWK']['antiSelection'].Integral())       
        histos['merged_EWK']['antiSelection'].SetLineColor(ROOT.kBlack)
        histos['merged_EWK']['antiSelection'].SetLineStyle(ROOT.kDashed)
        histos['merged_EWK']['antiSelection'].SetMaximum(1)
        histos['merged_EWK']['antiSelection'].SetMinimum(0.01)
        leg.AddEntry(histos['merged_EWK']['antiSelection'],'EWK anti-selected','l')
 
#        if histos['merged_EWK']['Selection'].Integral()>0:
#          histos['merged_EWK']['Selection'].Scale(1./histos['merged_EWK']['Selection'].Integral())             
        histos['merged_EWK']['Selection'].SetLineColor(ROOT.kBlack)
        histos['merged_EWK']['Selection'].SetMaximum(1)
        histos['merged_EWK']['Selection'].SetMinimum(0.01)
        leg.AddEntry(histos['merged_EWK']['Selection'],'EWK selected','l')
        
        histos['merged_QCD']['antiSelection'].Draw()
        histos['merged_QCD']['Selection'].Draw('same')
        histos['merged_EWK']['antiSelection'].Draw('same')
        histos['merged_EWK']['Selection'].Draw('same')
          
        leg.Draw()
        text.DrawLatex(0.15,.96,"CMS Simulation")
        text.DrawLatex(0.65,0.96,"L="+str(target_lumi/1000)+" fb^{-1} (13 TeV)")
        
        mergeCanv.cd()
        mergeCanv.Print(wwwDir+presel+SRname+'.png')
        mergeCanv.Print(wwwDir+presel+SRname+'.root')
        mergeCanv.Print(wwwDir+presel+SRname+'.pdf')


#path = '/data/'+username+'/results2015/rCS_0b/'
#if not os.path.exists(path):
#  os.makedirs(path)
#pickle.dump(bins, file(path+'QCDyieldFromTemplateFit_inclusiveHTandST_pkl','w'))
