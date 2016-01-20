from btagEfficiency import *
from math import *

def calc_btag_systematics(t,s,r,mcEffDict,sampleKey,maxConsideredBTagWeight,separateBTagWeights):
  #separateBTagWeights = False
  zeroTagWeight = 1.
  mceff = getMCEfficiencyForBTagSF(t, mcEffDict[sampleKey], sms='')
  #print
  #print mceff["mceffs"]
  mceffW                = getTagWeightDict(mceff["mceffs"], maxConsideredBTagWeight)
  mceffW_SF             = getTagWeightDict(mceff["mceffs_SF"], maxConsideredBTagWeight)
  mceffW_SF_b_Up        = getTagWeightDict(mceff["mceffs_SF_b_Up"], maxConsideredBTagWeight)
  mceffW_SF_b_Down      = getTagWeightDict(mceff["mceffs_SF_b_Down"], maxConsideredBTagWeight)
  mceffW_SF_light_Up    = getTagWeightDict(mceff["mceffs_SF_light_Up"], maxConsideredBTagWeight)
  mceffW_SF_light_Down  = getTagWeightDict(mceff["mceffs_SF_light_Down"], maxConsideredBTagWeight)
  if not separateBTagWeights:
    lweight = str(s.weight)
  else: lweight = "(1.)"
  #if not separateBTagWeights:
  for i in range(1, maxConsideredBTagWeight+2):
    exec("s.weightBTag"+str(i)+"p="+lweight)
    exec("s.weightBTag"+str(i)+"p_SF="+lweight)
    exec("s.weightBTag"+str(i)+"p_SF_b_Up="+lweight)
    exec("s.weightBTag"+str(i)+"p_SF_b_Down="+lweight)
    exec("s.weightBTag"+str(i)+"p_SF_light_Up="+lweight)
    exec("s.weightBTag"+str(i)+"p_SF_light_Down="+lweight)
  for i in range(maxConsideredBTagWeight+1):
    exec("s.weightBTag"+str(i)+"="              +str(mceffW[i])+'*'+lweight)
    exec("s.weightBTag"+str(i)+"_SF="           +str(mceffW_SF[i])+'*'+lweight)
    exec("s.weightBTag"+str(i)+"_SF_b_Up="      +str(mceffW_SF_b_Up[i])+'*'+lweight)
    exec("s.weightBTag"+str(i)+"_SF_b_Down="    +str(mceffW_SF_b_Down[i])+'*'+lweight)
    exec("s.weightBTag"+str(i)+"_SF_light_Up="  +str(mceffW_SF_light_Up[i])+'*'+lweight)
    exec("s.weightBTag"+str(i)+"_SF_light_Down="+str(mceffW_SF_light_Down[i])+'*'+lweight)
    for j in range(i+1, maxConsideredBTagWeight+2):
      exec("s.weightBTag"+str(j)+"p               -="+str(mceffW[i])+'*'+lweight) #prob. for >=j b-tagged jets
      exec("s.weightBTag"+str(j)+"p_SF            -="+str(mceffW_SF[i])+'*'+lweight)
      exec("s.weightBTag"+str(j)+"p_SF_b_Up       -="+str(mceffW_SF_b_Up[i])+'*'+lweight)
      exec("s.weightBTag"+str(j)+"p_SF_b_Down     -="+str(mceffW_SF_b_Down[i])+'*'+lweight)
      exec("s.weightBTag"+str(j)+"p_SF_light_Up   -="+str(mceffW_SF_light_Up[i])+'*'+lweight)
      exec("s.weightBTag"+str(j)+"p_SF_light_Down -="+str(mceffW_SF_light_Down[i])+'*'+lweight)
  for i in range (int(r.nJet)+1, maxConsideredBTagWeight+1):
    exec("s.weightBTag"+str(i)+"               = 0.")
    exec("s.weightBTag"+str(i)+"_SF            = 0.")
    exec("s.weightBTag"+str(i)+"_SF_b_Up       = 0.")
    exec("s.weightBTag"+str(i)+"_SF_b_Down     = 0.")
    exec("s.weightBTag"+str(i)+"_SF_light_Up   = 0.")
    exec("s.weightBTag"+str(i)+"_SF_light_Down = 0.")
    exec("s.weightBTag"+str(i)+"p              = 0.")
    exec("s.weightBTag"+str(i)+"p_SF           = 0.")
    exec("s.weightBTag"+str(i)+"p_SF_b_Up      = 0.")
    exec("s.weightBTag"+str(i)+"p_SF_b_Down    = 0.")
    exec("s.weightBTag"+str(i)+"p_SF_light_Up  = 0.")
    exec("s.weightBTag"+str(i)+"p_SF_light_Down= 0.")
  return

def calc_LeptonScale_factors_and_systematics(s,histos_LS):
  mu_mediumID_histo   =histos_LS['mu_mediumID_histo']
  mu_looseID_histo    =histos_LS['mu_looseID_histo']
  mu_miniIso02_histo  =histos_LS['mu_miniIso02_histo']
  mu_sip3d_histo      =histos_LS['mu_sip3d_histo']
  ele_cutbased_histo  =histos_LS['ele_cutbased_histo']
  ele_miniIso01_histo =histos_LS['ele_miniIso01_histo']
  if s.singleMuonic and s.leptonPt<120:
    bin_lepton_muSF_mediumID = mu_mediumID_histo.FindBin(s.leptonPt,abs(s.leptonEta))
    s.lepton_muSF_mediumID =  mu_mediumID_histo.GetBinContent(bin_lepton_muSF_mediumID)
    s.lepton_muSF_looseID =  mu_looseID_histo.GetBinContent(mu_looseID_histo.FindBin(s.leptonPt,abs(s.leptonEta)))
    s.lepton_muSF_miniIso02 =  mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(s.leptonPt,abs(s.leptonEta)))         
    s.lepton_muSF_sip3d =  mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(s.leptonPt,abs(s.leptonEta)))
    s.lepton_muSF_mediumID_err =  mu_mediumID_histo.GetBinError(mu_mediumID_histo.FindBin(s.leptonPt,abs(s.leptonEta)))
    s.lepton_muSF_looseID_err =  mu_looseID_histo.GetBinError(mu_looseID_histo.FindBin(s.leptonPt,abs(s.leptonEta)))
    s.lepton_muSF_miniIso02_err =  mu_miniIso02_histo.GetBinError(mu_miniIso02_histo.FindBin(s.leptonPt,abs(s.leptonEta)))       
    s.lepton_muSF_sip3d_err =  mu_sip3d_histo.GetBinError(mu_sip3d_histo.FindBin(s.leptonPt,abs(s.leptonEta)))
  if s.singleMuonic and s.leptonPt>=120:
    bin_lepton_muSF_mediumID = mu_mediumID_histo.FindBin(119,abs(s.leptonEta))
    s.lepton_muSF_mediumID =  mu_mediumID_histo.GetBinContent(bin_lepton_muSF_mediumID)
    s.lepton_muSF_looseID =  mu_looseID_histo.GetBinContent(mu_looseID_histo.FindBin(119,abs(s.leptonEta)))
    s.lepton_muSF_miniIso02 =  mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(119,abs(s.leptonEta)))
    s.lepton_muSF_sip3d =  mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(119,abs(s.leptonEta)))
    s.lepton_muSF_mediumID_err =  mu_mediumID_histo.GetBinError(mu_mediumID_histo.FindBin(119,abs(s.leptonEta)))
    s.lepton_muSF_looseID_err =  mu_looseID_histo.GetBinError(mu_looseID_histo.FindBin(119,abs(s.leptonEta)))
    s.lepton_muSF_miniIso02_err =  mu_miniIso02_histo.GetBinError(mu_miniIso02_histo.FindBin(119,abs(s.leptonEta)))
  if s.singleElectronic:
    s.lepton_eleSF_cutbasedID = ele_cutbased_histo.GetBinContent(ele_cutbased_histo.FindBin(s.leptonEt,abs(s.leptonEta)))      
    s.lepton_eleSF_miniIso01 = ele_miniIso01_histo.GetBinContent(ele_miniIso01_histo.FindBin(s.leptonEt,abs(s.leptonEta)))
    s.lepton_eleSF_cutbasedID_err = ele_cutbased_histo.GetBinError(ele_cutbased_histo.FindBin(s.leptonEt,abs(s.leptonEta)))
    s.lepton_eleSF_miniIso01_err = ele_miniIso01_histo.GetBinError(ele_miniIso01_histo.FindBin(s.leptonEt,abs(s.leptonEta)))
  return


def calc_TopPt_Weights(s,genParts):
  genTops = filter(lambda g:abs(g['pdgId'])==6, genParts)
  s.nGenTops = len(genTops)
  GenAntiTopIdx = -999
  GenTopIdx = -999
  for i_part, genPart in enumerate(genParts):
    if genPart['pdgId'] ==  6:
          s.GenTopPt = genPart['pt']
          GenTopIdx = i_part
    if genPart['pdgId'] == -6:
          s.GenAntiTopPt = genPart['pt']
          GenAntiTopIdx = i_part

  if s.GenTopPt!=-999 and s.GenAntiTopPt!=-999 and s.nGenTops==2:
    #print "genTop" , s.GenTopPt
    SFTop     = exp(0.156    -0.00137*s.GenTopPt    )
    SFAntiTop = exp(0.156    -0.00137*s.GenAntiTopPt)
    #print "SFTOP" , SFTop
    s.TopPtWeight = sqrt(SFTop*SFAntiTop)
    if s.TopPtWeight<0.5: s.TopPtWeight=0.5

    if GenAntiTopIdx!=-999 and GenTopIdx!=-999:
      genTop_vec = ROOT.TLorentzVector()
      genTop_vec.SetPtEtaPhiM(genParts[GenTopIdx]['pt'],genParts[GenTopIdx]['eta'],genParts[GenTopIdx]['phi'],genParts[GenTopIdx]['mass'])
      genAntiTop_vec = ROOT.TLorentzVector()
      genAntiTop_vec.SetPtEtaPhiM(genParts[GenAntiTopIdx]['pt'],genParts[GenAntiTopIdx]['eta'],genParts[GenAntiTopIdx]['phi'],genParts[GenAntiTopIdx]['mass'])
      GenTTBarp4 = genTop_vec + genAntiTop_vec
      s.GenTTBarPt = GenTTBarp4.Pt()
      if s.GenTTBarPt>120: s.GenTTBarWeight= 0.95
      if s.GenTTBarPt>150: s.GenTTBarWeight= 0.90
      if s.GenTTBarPt>250: s.GenTTBarWeight= 0.80
      if s.GenTTBarPt>400: s.GenTTBarWeight= 0.70 
      #print s.GenTTBarPt , s.GenTTBarWeight
  return


def calcDLDictionary(s,r,keepIdx , discardIdx ,tightHardLep):
   out_dict = {}

   met_4vec = ROOT.TLorentzVector()
   met_4vec.SetPtEtaPhiM(r.met_pt,r.met_eta,r.met_phi,r.met_mass)
   met_2vec = ROOT.TVector2(met_4vec.Px(),met_4vec.Py())
   lepToDiscard4D = ROOT.TLorentzVector()
   lepToDiscard4D.SetPtEtaPhiM(tightHardLep[discardIdx]['pt'],tightHardLep[discardIdx]['eta'],tightHardLep[discardIdx]['phi'],tightHardLep[discardIdx]['mass'])
   lepToKeep4D = ROOT.TLorentzVector()
   lepToKeep4D.SetPtEtaPhiM(tightHardLep[keepIdx]['pt'],tightHardLep[keepIdx]['eta'],tightHardLep[keepIdx]['phi'],tightHardLep[keepIdx]['mass'])

   lepToDiscard2D = ROOT.TVector2(lepToDiscard4D.Px(),lepToDiscard4D.Py())
   lepToKeep2D = ROOT.TVector2(lepToKeep4D.Px(),lepToKeep4D.Py())

   Met2D_AddFull = met_2vec + lepToDiscard2D #adding lost lepton pt to met
   Met2D_AddThird = met_2vec + (1/3.*lepToDiscard2D)
   out_dict["LepToKeep_pt"] = lepToKeep2D.Mod()
   out_dict["LepToKeep_eta"] = lepToKeep4D.Eta()
   out_dict["LepToKeep_Et"] = lepToKeep4D.Et()
   out_dict["lepToDiscard_pt"] = lepToDiscard2D.Mod()
   out_dict["lepToDiscard_eta"] = lepToDiscard4D.Eta()
   out_dict["lepToDiscard_Et"] = lepToDiscard4D.Et()

   DL_dPhiLepW = {}
   DL_ST = {}
   DL_HT = {}
   DL_nJet = {}

   recoWp4 = lepToKeep2D + met_2vec
   DL_dPhiLepW["notAddLepMet"] = lepToKeep2D.DeltaPhi(recoWp4) # [0]: not adding leptons to MET
   DL_ST["notAddLepMet"] = lepToKeep2D.Mod() + met_2vec.Mod()
   DL_HT["notAddLepMet"] = s.htJet30j
   DL_nJet["notAddLepMet"] = s.nJet30

   recoWp4_AddFull = lepToKeep2D + Met2D_AddFull
   DL_dPhiLepW["AddLepMet"] = lepToKeep2D.DeltaPhi(recoWp4_AddFull) # [0]: adding lost lepton pt to met
   DL_ST["AddLepMet"] = lepToKeep2D.Mod() + Met2D_AddFull.Mod()
   dlht = s.htJet30j + (lepToDiscard2D.Mod() if lepToDiscard2D.Mod()>30. else 0.)
   DL_HT["AddLepMet"] = dlht
   njet_new = s.nJet30 + (1 if lepToDiscard2D.Mod()>30. else 0.)
   DL_nJet["AddLepMet"] = njet_new

   recoWp4_AddThird = lepToKeep2D + Met2D_AddThird
   DL_dPhiLepW["AddLep1ov3Met"] = lepToKeep2D.DeltaPhi(recoWp4_AddThird) # [2]: adding 1/3 of lepton ptto met 
   DL_ST["AddLep1ov3Met"] = lepToKeep2D.Mod() + Met2D_AddThird.Mod()
   dlht = s.htJet30j + (2/3.*lepToDiscard2D.Mod() if 2/3.*lepToDiscard2D.Mod()>30 else 0.)
   DL_HT["AddLep1ov3Met"] = dlht
   njet_new = s.nJet30 + (1 if 2/3.*lepToDiscard2D.Mod()>30 else 0.)
   DL_nJet["AddLep1ov3Met"] = njet_new

   out_dict["l1l2ovMET"]    =  (tightHardLep[0]['pt'] + tightHardLep[1]['pt'])/met_4vec.Pt()
   out_dict["Vecl1l2ovMET"] = (lepToKeep2D + lepToDiscard2D).Mod()/met_4vec.Pt()
   out_dict["DPhil1l2"]     = lepToKeep2D.DeltaPhi(lepToDiscard2D)


   out_dict["DL_dPhiLepW"] = DL_dPhiLepW
   out_dict["DL_ST"] = DL_ST
   out_dict["DL_HT"] = DL_HT
   out_dict["DL_nJet"] = DL_nJet


   #print out_dict

   return out_dict


def calc_diLep_contributions(s,r,tightHardLep,rand_input,histos_LS):
  if s.nTightHardLeptons==2:
    #print "n lepton :" , s.nTightHardLeptons
    passSel = False
    lep1_vec = ROOT.TLorentzVector()
    lep1_vec.SetPtEtaPhiM(tightHardLep[0]['pt'],tightHardLep[0]['eta'],tightHardLep[0]['phi'],tightHardLep[0]['mass'])
    lep2_vec = ROOT.TLorentzVector()
    lep2_vec.SetPtEtaPhiM(tightHardLep[1]['pt'],tightHardLep[1]['eta'],tightHardLep[1]['phi'],tightHardLep[1]['mass'])
    ll_vec = lep1_vec+lep2_vec
    #print tightHardLep[0]['pdgId'] , lep1_vec.M() , lep2_vec.M() , lep2_vec.Pt() ,ll_vec.M()
    if tightHardLep[0]['charge'] != tightHardLep[1]['charge']: passSel = True
    if (tightHardLep[0]['pdgId'] == -tightHardLep[1]['pdgId']) and abs(ll_vec.M()-91.2)<10. : passSel = False
    if passSel:
      random = ROOT.TRandom2(int(rand_input))
      uniform01 = random.Rndm()
      #print "uniform:" , uniform01
      lepToKeep = int(uniform01>0.5)
      #print "leptokeep: " , lepToKeep
      s.LepToKeep_pdgId = tightHardLep[lepToKeep]["pdgId"]
      lepToDiscard = int(not lepToKeep)
      s.lepToDiscard_pdgId = tightHardLep[lepToDiscard]["pdgId"]
      aktions = ["notAddLepMet" , "AddLepMet" , "AddLep1ov3Met"]
      var_DLs = ["ST","HT","dPhiLepW","nJet"]
      keepIdx=lepToDiscard
      discardIdx=lepToKeep
      outdict = calcDLDictionary(s,r, keepIdx ,discardIdx ,tightHardLep)
      #print "after the fuction:" , outdict
      for action in aktions:
        for var_DL in var_DLs :
          #print "s.DL_"+var_DL+"_lepToDiscard_"+action
          exec("s.DL_"+var_DL+"_lepToDiscard_"+action+"="+str(outdict["DL_"+var_DL][action]))

      s.l1l2ovMET_lepToDiscard   = outdict["l1l2ovMET"]
      s.Vecl1l2ovMET_lepToDiscard = outdict["Vecl1l2ovMET"]
      s.DPhil1l2_lepToDiscard  = outdict["DPhil1l2"]

      keepIdx=lepToKeep
      discardIdx=lepToDiscard
      outdict = calcDLDictionary(s,r, keepIdx ,discardIdx ,tightHardLep)
      for action in aktions:
        for var_DL in var_DLs :
          #print "s.DL_"+var_DL+"_lepToKeep_"+action
          exec("s.DL_"+var_DL+"_lepToKeep_"+action+"="+str(outdict["DL_"+var_DL][action]))

      s.l1l2ovMET_lepToKeep   = outdict["l1l2ovMET"]
      s.Vecl1l2ovMET_lepToKeep= outdict["Vecl1l2ovMET"]
      s.DPhil1l2_lepToKeep    = outdict["DPhil1l2"]

      s.LepToKeep_pt = outdict["LepToKeep_pt"]
      ####calculate the lepton scale eff for each lepton####
      mu_mediumID_histo   =histos_LS['mu_mediumID_histo']
      mu_miniIso02_histo  =histos_LS['mu_miniIso02_histo']
      mu_sip3d_histo      =histos_LS['mu_sip3d_histo']
      ele_cutbased_histo  =histos_LS['ele_cutbased_histo']
      ele_miniIso01_histo =histos_LS['ele_miniIso01_histo']

      if abs(s.LepToKeep_pdgId)==11 : s.LepToKeep_eleSF = ele_cutbased_histo.GetBinContent(ele_cutbased_histo.FindBin(outdict["LepToKeep_Et"],abs(outdict["LepToKeep_eta"])))*(ele_miniIso01_histo.GetBinContent(ele_miniIso01_histo.FindBin(outdict["LepToKeep_Et"],abs(outdict["LepToKeep_eta"])))) 

      if abs(s.LepToKeep_pdgId)==13 and outdict["LepToKeep_pt"]>=120: s.LepToKeep_muSF =mu_mediumID_histo.GetBinContent(mu_mediumID_histo.FindBin(119,abs(outdict["LepToKeep_eta"])))*(mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(119,abs(outdict["LepToKeep_eta"]))))*(mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(119,abs(outdict["LepToKeep_eta"]))))
      if abs(s.LepToKeep_pdgId)==13 and outdict["LepToKeep_pt"]<120: s.LepToKeep_muSF =mu_mediumID_histo.GetBinContent(mu_mediumID_histo.FindBin(outdict["LepToKeep_pt"],abs(outdict["LepToKeep_eta"])))*(mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(outdict["LepToKeep_pt"],abs(outdict["LepToKeep_eta"]))))*(mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(outdict["LepToKeep_pt"],abs(outdict["LepToKeep_eta"]))))

      if abs(s.lepToDiscard_pdgId)==11 : s.lepToDiscard_eleSF = ele_cutbased_histo.GetBinContent(ele_cutbased_histo.FindBin(outdict["lepToDiscard_Et"],abs(outdict["lepToDiscard_eta"])))*(ele_miniIso01_histo.GetBinContent(ele_miniIso01_histo.FindBin(outdict["lepToDiscard_Et"],abs(outdict["lepToDiscard_eta"]))))

      if abs(s.lepToDiscard_pdgId)==13 and outdict["lepToDiscard_pt"]>=120 : s.lepToDiscard_muSF =mu_mediumID_histo.GetBinContent(mu_mediumID_histo.FindBin(119,abs(outdict["lepToDiscard_eta"])))*(mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(119,abs(outdict["lepToDiscard_eta"]))))*(mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(119,abs(outdict["lepToDiscard_eta"]))))
      if abs(s.lepToDiscard_pdgId)==13 and outdict["lepToDiscard_pt"]<120 : s.lepToDiscard_muSF = mu_mediumID_histo.GetBinContent(mu_mediumID_histo.FindBin(outdict["lepToDiscard_pt"],abs(outdict["lepToDiscard_eta"])))*(mu_miniIso02_histo.GetBinContent(mu_miniIso02_histo.FindBin(outdict["lepToDiscard_pt"],abs(outdict["lepToDiscard_eta"]))))*(mu_sip3d_histo.GetBinContent(mu_sip3d_histo.FindBin(outdict["lepToDiscard_pt"],abs(outdict["lepToDiscard_eta"]))))


  return
