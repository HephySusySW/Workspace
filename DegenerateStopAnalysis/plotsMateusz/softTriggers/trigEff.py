import ROOT
import os, sys
import math
import argparse
import pickle
from array import array
from math import pi, sqrt #cos, sin, sinh, log

from DataFormats.FWLite import Events, Handle

ROOT.gStyle.SetOptStat(0) #0 removes histogram statistics box #Name, Entries, Mean, RMS, Underflow, Overflow, Integral, Skewness, Kurtosis
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptFit(1111) #1111 prints fits results on plot

ROOT.gStyle.SetPaintTextFormat("4.2f")
#ROOT.gStyle->SetTitleX(0.1)
#ROOT.gStyle->SetTitleW(0.8)

ROOT.gStyle.SetStatX(0.875)
ROOT.gStyle.SetStatY(0.75)
ROOT.gStyle.SetStatW(0.1)
ROOT.gStyle.SetStatH(0.1)

savedir = "/afs/hephy.at/user/m/mzarucki/www/plots/TriggerStudies"

infiles = ['/afs/hephy.at/data/mzarucki02/TriggerStudies/CMSSW_9_2_12/AOD/T2tt_dM-10to80_mStop-500_mLSP-460_SoftTriggers-V15_AODSIM/T2tt_dM-10to80_mStop-500_mLSP-460_SoftTriggers-V15_AODSIM_%s.root'%(i+1) for i in range(100)]
#infiles = ['/afs/hephy.at/data/mzarucki02/TriggerStudies/CMSSW_9_2_12/AOD/WJetsToLNu_RunIISummer17DRStdmix_92X_upgrade2017_realistic_v10-v1_SoftTriggers-V15_AODSIM_small/WJetsToLNu_RunIISummer17DRStdmix_92X_upgrade2017_realistic_v10-v1_SoftTriggers-V15_AODSIM_small_%s.root'%(i+1) for i in range(50)]
#infile = '/afs/hephy.at/data/mzarucki02/TriggerStudies/CMSSW_9_2_12/AOD/T2tt_dM-10to80_mStop-500_mLSP-460_noPU_SoftTriggers_V9_HLT_AODSIM.root'
triggerList = "SoftTriggers_V15.list"

doFit = True

# Functions

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        #if exc.errno == errno.EEXIST and os.path.isdir(path):
        if os.path.isdir(path):
            pass
        else:
            raise

def makeDir(path):
    if "." in path[-5:]:
        path = path.replace(os.path.basename(path),"")
        print path
    if os.path.isdir(path):
        return
    else:
        mkdir_p(path)

def getListFromFile(filename):
   f = open(filename,'r')
   outlist = []
   for l in f:
      l = l.strip('\n')
      outlist.append(l)
   f.close()
   return outlist

# Efficiency
def makeEffPlot(passed,total):
   a = passed.Clone()
   b = total.Clone()
   eff = ROOT.TEfficiency(a,b)
   eff.SetTitle("Efficiency Plot")
   eff.SetMarkerStyle(33)
   eff.SetMarkerSize(2)
   eff.SetLineWidth(2)
   return eff

def setupEffPlot(eff):
   ROOT.gPad.Modified()
   ROOT.gPad.Update()

   ROOT.gPad.SetGridx()
   ROOT.gPad.SetGridy()
   eff.GetPaintedGraph().GetYaxis().SetTitle("Efficiency")
   eff.GetPaintedGraph().SetMinimum(0)
   eff.GetPaintedGraph().SetMaximum(1)
   eff.GetPaintedGraph().GetXaxis().CenterTitle()
   eff.GetPaintedGraph().GetYaxis().CenterTitle()

   ROOT.gPad.Modified()
   ROOT.gPad.Update()

def drawText(text, x, y):        
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.015)
    latex.DrawLatex(x,y, "#font[42]{%s}"%text)

triggers = getListFromFile(triggerList) 
variables = {'MET':'PFMET', 'HT':'PFHT', 'JetPt':'Jet', 'MuPt':'Mu', 'ElePt':'Ele'}

varsCutOn = {}
varsToPlot = {}
                
for trig in triggers:
    varsCutOn[trig] = []
    
    for var in variables:
        if variables[var] in trig:
            varsCutOn[trig].append(var)
    
    varsToPlot[trig] = varsCutOn[trig][:]
    
    if 'MET' in varsToPlot[trig] and not 'HT' in varsToPlot[trig]:
        varsToPlot[trig].append('HT')
    elif 'HT' in varsToPlot[trig] and not 'MET' in varsToPlot[trig]:
        varsToPlot[trig].append('MET')
    if 'HT' in varsToPlot[trig] and not 'JetPt' in varsToPlot[trig]:
        varsToPlot[trig].append('JetPt')

# Histograms
hists = {'dens':{}, 'nums':{}}
xmax = {'MET':500, 'HT':500, 'JetPt':300, 'MuPt':30, 'ElePt':30}

for var in variables:
    hists['dens'][var] = {}
    hists['nums'][var] = {}

    for trig in triggers:
        hists['dens'][var][trig] = ROOT.TH1D("den_%s_%s"%(var,trig), "den_%s_%s"%(var,trig), 100, 0, xmax[var])
        #hists['dens'][var][trig].SetTitle("%s Distribution"%var)
        hists['dens'][var][trig].GetYaxis().SetTitle("Events")
        hists['dens'][var][trig].GetXaxis().SetTitle("%s / GeV"%var)
        hists['dens'][var][trig].GetXaxis().CenterTitle()
        hists['dens'][var][trig].GetYaxis().CenterTitle()
        hists['dens'][var][trig].GetXaxis().SetTitleOffset(1.2)
        hists['dens'][var][trig].GetYaxis().SetTitleOffset(1.3)
        hists['dens'][var][trig].SetFillColor(ROOT.kBlue-9)
        hists['dens'][var][trig].SetLineColor(ROOT.kBlack)
        hists['dens'][var][trig].SetLineWidth(2)

        hists['nums'][var][trig] = ROOT.TH1D("num_%s_%s"%(var, trig), "num_%s_%s"%(var, trig), 100, 0, xmax[var])
        hists['nums'][var][trig].SetFillColor(ROOT.kGreen+2)
        hists['nums'][var][trig].SetLineColor(ROOT.kBlack)
        hists['nums'][var][trig].SetLineWidth(2)

#f = ROOT.TFile(infile)
#tree = f.Get("Events")

#nEvents = nListEntries
#nEvents = tree.GetEntries() 

# Handles to get event products
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::SoftTriggers")
handleMETs = Handle("std::vector<reco::PFMET>")
handleJets = Handle("std::vector<reco::PFJet>")
handleMus  = Handle('std::vector<reco::Muon>')
handleEles = Handle('std::vector<reco::GsfElectron>')

events = Events(infiles)

values = {}
plateauCuts = {'MuPt':8, 'ElePt':10, 'MET':100, 'HT':100, 'JetPt':100} 

lepEtaCut = 'EB'

if lepEtaCut not in ['EB', 'EE']:
    lepEtaCut = 'EBplusEE'

#for i in range(nEvents):
for i,event in enumerate(events):
    #print i
    #print "eList index", i
    #if i == 1000: break
    
    #tree.GetEntry(i)

    #tree.GetEntry(eList.GetEntry(i))
    #TTree:GetEntry(entry) = Read all branches of entry and return total number of bytes read. The function returns the number of bytes read from the input buffer. If entry does not exist the function returns 0. If an I/O error occurs,
    #TEventList:GetEntry(index) = Return value of entry at index in the list. Return -1 if index is not in the list range. 
    #TEventList:GetIndex(entry) Return index in the list of element with value entry array is supposed to be sorted prior to this call. If match is found, function returns position of element.
    
    #run = event.eventAuxiliary().run()
    #lumi = event.eventAuxiliary().luminosityBlock()
    #eventId = event.eventAuxiliary().event()
    
    # Muons 
    event.getByLabel(("muons", '', 'RECO'), handleMus)
    muons = handleMus.product()
    
    if len(muons) > 0: 
        values['MuPt'] = muons[0].pt()   
        
        if lepEtaCut == "EB":
            if not abs(muons[0].eta()) < 1.5: continue
        elif lepEtaCut == "EE":
            if not abs(muons[0].eta()) > 1.5: continue
    
    else:
        values['MuPt'] = -1
    
    # Electrons 
    event.getByLabel(("gedGsfElectrons", '', 'RECO'), handleEles)
    electrons = handleEles.product()
    
    if len(electrons) > 0: 
        values['ElePt'] = electrons[0].pt()   
    else:
        values['ElePt'] = -1
    
    # MET    
    event.getByLabel(("pfMet", '', 'RECO'), handleMETs)
    met = handleMETs.product().front()
    values['MET'] = met.pt()
    #MET = tree.GetLeaf("recoPFMETs_pfMet__RECO.obj").pt().GetValue(0)

    # Jets
    event.getByLabel(("ak4PFJets", '', 'RECO'), handleJets)
    jets = handleJets.product()
    if len(jets) > 0:
        values['JetPt'] = jets[0].pt()
    else:
        values['JetPt'] = -1
   
    # HT Calculation
    jetPtCut = 30.     
    jetEtaCut = 2.4   

    values['HT'] = 0.
    for jet in jets:
        if(jet.pt() > jetPtCut and abs(jet.eta()) < jetEtaCut): 
             values['HT'] += jet.pt()
    
    # Trigger Results
    event.getByLabel(triggerBitLabel, triggerBits)

    if i == 0:
        trigNames = event.object().triggerNames(triggerBits.product())
        triggers = []

        for trigName in trigNames.triggerNames():
            trigName = str(trigName)
            if ("HLTriggerFirstPath" in trigName) or ("HLTriggerFinalPath" in trigName): continue
            if not (trigName.startswith("HLT_") or trigName.startswith("DST_")): continue
            triggers.append(trigName)

    for trig in triggers:
        index = trigNames.triggerIndex(trig)
        decision = triggerBits.product().accept(index)
        #decision = tree.GetLeaf(tree.GetAlias(trig)).GetValue(0) # if trigger saved as branch via TriggerDecisionAnalyzer

        for plot in varsToPlot[trig]:
            passEvent = True
            for var in varsCutOn[trig]:
                if plot != var and values[var] < plateauCuts[var]:
                    passEvent = False

            if passEvent:
                hists['dens'][plot][trig].Fill(values[plot])
                if decision:
                    hists['nums'][plot][trig].Fill(values[plot])

# Fit Function
if doFit:
    fitFunc = ROOT.TF1("f1", "[0]*TMath::Erf((x-[1])/[2]) + [3]", 0, 1000) #Error function scaled to [0,1]
    fitFunc.SetParNames("Norm.", "Edge", "Resolution", "Y-Offset")
    #fitFunc.SetLineColor(ROOT.kAzure-1)
    #fitFunc.SetParameter(0, 0.5)
    #fitFunc.SetParameter(1, 150)
    #fitFunc.SetParameter(2, 50)  
    
    #fitFunc.SetParLimits(0, 0.4, 0.65) 
    #fitFunc.SetParLimits(1, 0, 100)
    #fitFunc.SetParLimits(2, 0, 50)
    #fitFunc.SetParLimits(3, 0.4, 0.8)
    
    #fitFunc.SetParameters(0.5, 30, 20, 0.5)
    #fitFunc.SetParameters(0.5, 140, 40, 0.50)

for trig in triggers:
    for var in varsToPlot[trig]:
        canv = ROOT.TCanvas("Canvas %s_%s"%(var,trig), "Canvas %s_%s"%(var,trig), 1500, 1500)
        canv.SetGrid()

        # Histograms
               
        hists['dens'][var][trig].Draw('hist')
        hists['nums'][var][trig].Draw('hist same')
        
        ROOT.gPad.Modified()
        ROOT.gPad.Update()
        
        latex1 = ROOT.TLatex()
        latex1.SetNDC()
        latex1.SetTextSize(0.03)
        latex1.DrawLatex(0.12, 0.92, "CMS Simulation")
        #latex1.DrawLatex(0.12, 0.92, "#font[62]{CMS Simulation}")
        
        latex2 = ROOT.TLatex()
        latex2.SetNDC()
        latex2.SetTextSize(0.025)
        latex2.SetTextColor(ROOT.kRed+1)
        latex2.DrawLatex(0.45, 0.85, trig)
            
        ## Efficiency

        overlay = ROOT.TPad("overlay", "", 0, 0, 1, 1)
        overlay.SetFillStyle(4000)
        overlay.SetFillColor(0)
        overlay.SetFrameFillStyle(4000)
        overlay.Draw()
        overlay.cd()

        frame = overlay.DrawFrame(0, 0, xmax[var], 1.1) # overlay.DrawFrame(pad.GetUxmin(), 0, pad.GetUxmax(), 1.2)
 
        eff = makeEffPlot(hists['nums'][var][trig],hists['dens'][var][trig])
        #eff.SetMarkerColor(ROOT.kAzure-1)
        #eff.SetTitle("%s Trigger Efficiency; %s; Trigger Efficiency"%(trig,var))
        eff.Draw("P")
       
        # axis on the right side
        axis = ROOT.TGaxis(ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUymax(), 510, "+L")
        axis.SetTitle("#font[42]{Trigger Efficiency}")
        axis.CenterTitle()
        axis.SetLabelSize(0.03)
        axis.SetTitleSize(0.03)
        axis.SetTitleOffset(1.4)
        axis.SetLabelColor(ROOT.kAzure-1)
        axis.SetLineColor(ROOT.kAzure-1)
        axis.SetTextColor(ROOT.kAzure-1)
        axis.Draw()

        if doFit:
    
            variables = {'MET':'PFMET', 'HT':'PFHT', 'JetPt':'Jet', 'MuPt':'Mu', 'ElePt':'Ele'}
            if var in ['MuPt', 'ElePt']: 
                fitFunc.SetParameters(0.5, 50, 50, 0.5)
            else:
                fitFunc.SetParameters(0.5, 5, 20, 0.5)

            eff.Fit(fitFunc)

            # Fit Parameter Extraction
            fitParams = {}
            #fitFunc.GetParameters(fit)
            fitParams['chiSq'] = fitFunc.GetChisquare()
            for x in xrange(0, 4):
               fitParams['var%s'%x] = fitFunc.GetParameter(x)
               fitParams['var%s'%x] = fitFunc.GetParError(x)
            
               fitParams['val50'] =  fitFunc.GetX(0.5)
               fitParams['val75'] =  fitFunc.GetX(0.75)
               fitParams['val80'] =  fitFunc.GetX(0.80)
               fitParams['val85'] =  fitFunc.GetX(0.85)
               fitParams['val90'] =  fitFunc.GetX(0.90)
               fitParams['val95'] =  fitFunc.GetX(0.95)
               fitParams['val99'] =  fitFunc.GetX(0.99)
               fitParams['val100'] = fitFunc.GetX(1)
       
            #print 'Fit parameters', var, trig, fitParams
 
            ROOT.gPad.Modified()
            ROOT.gPad.Update()
   
            setupEffPlot(eff)
        
            pad = ROOT.TPad("pad", "", 0, 0, 1, 1)
            pad.SetFillStyle(0)
            pad.Draw()
            pad.cd()
            
            box = ROOT.TBox(0.7, 0.35, 0.875, 0.525)
            box.SetFillColor(0)
            box.Draw('l')

            drawText("#bf{Turn-on:}", 0.75, 0.5)
            drawText("100 %%: %.0f GeV"%fitParams['val100'], 0.725, 0.475)
            drawText("  99 %%: %.0f GeV"%fitParams['val99'],  0.725, 0.45)
            drawText("  95 %%: %.0f GeV"%fitParams['val95'],  0.725, 0.425)
            drawText("  90 %%: %.0f GeV"%fitParams['val90'],  0.725, 0.4)
            drawText("  85 %%: %.0f GeV"%fitParams['val85'],  0.725, 0.375)
 
            ROOT.gPad.Modified()
            ROOT.gPad.Update()
 
        #Save canvas
        finalSavedir = "%s/%s/%s"%(savedir,trig, lepEtaCut)
        makeDir("%s/root"%finalSavedir) 
        makeDir("%s/pdf"%finalSavedir)
 
        canv.SaveAs("%s/trigEff_%s_%s.png"%(finalSavedir,var,trig))
        canv.SaveAs("%s/pdf/trigEff_%s_%s.pdf"%(finalSavedir,var,trig))
        canv.SaveAs("%s/root/trigEff_%s_%s.root"%(finalSavedir,var,trig))
