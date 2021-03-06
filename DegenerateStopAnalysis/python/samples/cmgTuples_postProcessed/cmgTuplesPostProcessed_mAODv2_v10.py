""" Sample definition file for CMG post-processed ntuples using 2016 data and MC production at 25 ns for the degenerate stop analysis.
 
Each set of ntuples is produced with a git tag of HephySusySW.Workspace repository and and is saved in a directory:
  
   {path}/cmgTuples/{processingEra}/{processingTag}/{campaign}/{inc/soft/...}
   
    processingEra: postProcessed_mAODv2_v* (always starts with "postProcessed_")
    processingTag: 80X_postProcessing_v* (git tag of HephySusySW.Workspace)
    
    campaign:
        MC production campaign for MC samples  (e.g. RunIISpring16MiniAODv2, with _25ns added as additional identification)
        Energy, reconstruction tag, era for data (e.g. 13TeV_PromptReco_Collisions15_25ns, taken from JSON name file)
    
The corresponding py sample files are called: 
    RunIISpring16MiniAODv2_v*.py 
    Data2016_v*.py

"""

import copy
import os
import sys
import pickle
import importlib
 
# most recent paths, can be replaced when initializing the cmgTuplesPostProcessed class
ppDir = '/afs/hephy.at/data/mzarucki02/cmgTuples/postProcessed_mAODv2/8025_mAODv2_v10/80X_postProcessing_v0/analysisHephy_13TeV_2016_v2_6/step1'
mc_path     = ppDir + "/RunIISummer16MiniAODv2_v10"
data_path   = ppDir + "/Data2016_v10"
signal_path = mc_path

# Lumi that was used in the weight calculation of PostProcessing in pb-1
lumi_mc = 10000.

class cmgTuplesPostProcessed():

    def makeSample(self, sample):
        i = copy.deepcopy(sample)
        i['dir'] = os.path.join(i['dir'], 'inc')

        pold = copy.deepcopy(sample)
        pold['dir'] = os.path.join(pold['dir'], 'preselection', 'inc')

        p = copy.deepcopy(sample)
        p['dir'] = os.path.join(p['dir'], 'skimPreselect', 'inc')
        
        il = copy.deepcopy(sample)
        il['dir'] = os.path.join(il['dir'], 'incLep')

        ol = copy.deepcopy(sample)
        ol['dir'] = os.path.join(ol['dir'], 'oneLep')
        
        ol20 = copy.deepcopy(sample)
        ol20['dir'] = os.path.join(ol20['dir'], 'oneLep20')
        
        olg = copy.deepcopy(sample)
        olg['dir'] = os.path.join(olg['dir'], 'oneLepGood')
        
        olg20 = copy.deepcopy(sample)
        olg20['dir'] = os.path.join(olg20['dir'], 'oneLepGood20')
        
        olg_ht800 = copy.deepcopy(sample)
        olg_ht800['dir'] = os.path.join(olg_ht800['dir'], 'oneLepGood_HT800')
        
        olg_ht100_met40_mt30 = copy.deepcopy(sample)
        olg_ht100_met40_mt30['dir'] = os.path.join(olg_ht100_met40_mt30['dir'], 'oneLepGood_HT100_MET40_MT30')
        
        oelg50_isr100_met40_mt30 = copy.deepcopy(sample)
        oelg50_isr100_met40_mt30['dir'] = os.path.join(oelg50_isr100_met40_mt30['dir'], 'oneElGood50_ISR100_MET40_MT30')
        
        met200 = copy.deepcopy(sample)
        met200['dir'] = os.path.join(met200['dir'], 'met200')

        pil = copy.deepcopy(sample)
        pil['dir'] = os.path.join(pil['dir'], 'skimPreselect', 'incLep')
        
        sf = copy.deepcopy(sample)
        sf['dir'] = os.path.join(sf['dir'], 'skimPreselect', 'filterInc')

        pif = copy.deepcopy(sample)
        pif['dir'] = os.path.join(pif['dir'], 'skimPreselect', 'filter')

        pifsrcr = copy.deepcopy(sample)
        pifsrcr['dir'] = os.path.join(pifsrcr['dir'], 'skimPreselect', 'filterMETHT250')

        pifsrcrjec = copy.deepcopy(sample)
        pifsrcrjec['dir'] = os.path.join(pifsrcrjec['dir'], 'skimPreselect', 'filterMETHT250JEC')

        pifjec = copy.deepcopy(sample)
        pifjec['dir'] = os.path.join(pifjec['dir'], 'skimPreselect', 'filterJEC')

        pifmll = copy.deepcopy(sample)
        pifmll['dir'] = os.path.join(pifmll['dir'], 'skimPreselect', 'filterMLL')


        #pifsrcr = copy.deepcopy(sample)
        #pifsrcr['dir'] = os.path.join(pifsrcr['dir'], 'skimPreselect', 'filterMETHT250_FS')

        pol = copy.deepcopy(sample)
        pol['dir'] = os.path.join(pol['dir'], 'skimPreselect', 'oneLepGood')

        badmu = copy.deepcopy(sample)
        badmu['dir'] = os.path.join(badmu['dir'], 'twoMu_MET100')

        lt120 = copy.deepcopy(sample)
        lt120['dir'] = os.path.join(lt120['dir'], 'LT120')

        return {
            'inc': i,
            #'preOneLep': pold,
            'skimPresel': p,
            'incLep': il,
            'oneLep': ol,
            'oneLep20': ol20,
            'oneLepGood': olg,
            'oneLepGood20': olg20,
            'oneLepGood_HT800': olg_ht800,
            'oneLepGood_HT100_MET40_MT30': olg_ht100_met40_mt30,
            'oneElGood50_ISR100_MET40_MT30': oelg50_isr100_met40_mt30,
            'met200': met200,
            'preIncLep': pil,
            'preSF': sf,
            'preOneLep':  pol, 
            'lt120'    : lt120,
            'twoMu'    : badmu,
            'filter'   : pif,
            'filterMETHT250'   : pifsrcr,
            'filterMETHT250JEC'   : pifsrcrjec,
            'filterJEC'   : pifjec,
            'filterMLL'   : pifmll,
            }

    def getDataSample(self, name, bins):
        s = self.makeSample({
            "name" : name,
            "bins" : [bins] if type(bins)==type("") else bins,
            'dir' : self.data_path,
            })
        #
        return s

    def getSignalSample(self, signal, sampleId=0):
        return {
            "name" : signal,
            "chunkString": signal,
            'dir' : self.signal_path,
            'bins':[signal],
            'sampleId' : sampleId,
            }

    def __init__(self, mc_path=mc_path, signal_path=signal_path, data_path=data_path, lumi_mc=lumi_mc , ichepdata=False):

        self.mc_path = mc_path
        self.signal_path = signal_path
        self.data_path = data_path
        self.lumi = lumi_mc
        self.ichepdata = ichepdata

        print "MC DIR:      ", self.mc_path
        print "SIGNAL DIR:  ", self.signal_path
        print "DATA DIR:    ", self.data_path


        self.TT_pow = self.makeSample({
            "name" : "TT_pow",
            "bins" : [
                        'TT_pow',
                        'TT_pow_backup',
                ],
            'dir' : self.mc_path,
            'sampleId' : 20,
            })
        
        self.TTJets_SingleLepton = self.makeSample({
            "name" : "TTJets_SingleLepton",
            "bins" : [
                         'TTJets_SingleLeptonFromT',
                         'TTJets_SingleLeptonFromT_ext',
                         'TTJets_SingleLeptonFromTbar',
                         'TTJets_SingleLeptonFromTbar_ext',
                ],
            'dir' : self.mc_path,
            'sampleId': 65,
            })

        self.TTJets_DiLepton = self.makeSample({
            "name" : "TTJets_DiLepton",
            "bins" : [
                         'TTJets_DiLepton',
                         'TTJets_DiLepton_ext',
                ],
            'dir' : self.mc_path,
            'sampleId': 70,
            })

        self.TTX = self.makeSample({
            "name" : "ttx",
            "bins" : [
                        'TTGJets',
                        'TTW_LO', 
                        'TTZ_LO',
                ],
            'dir' : self.mc_path,
            'sampleId': 90,
            })

        self.WJetsHT = self.makeSample({
            "name" : "WJetsHT",
            "bins" : [
                      'WJetsToLNu_HT70to100',
                      'WJetsToLNu_HT100to200',
                      'WJetsToLNu_HT100to200_ext',
                      'WJetsToLNu_HT100to200_ext2',
                      'WJetsToLNu_HT200to400',
                      'WJetsToLNu_HT200to400_ext',
                      'WJetsToLNu_HT200to400_ext2',
                      'WJetsToLNu_HT400to600',
                      'WJetsToLNu_HT400to600_ext',
                      'WJetsToLNu_HT600to800',
                      'WJetsToLNu_HT600to800_ext',
                      'WJetsToLNu_HT800to1200',
                      'WJetsToLNu_HT800to1200_ext',
                      'WJetsToLNu_HT1200to2500',
                      'WJetsToLNu_HT1200to2500_ext',
                      'WJetsToLNu_HT2500toInf',
                      'WJetsToLNu_HT2500toInf_ext',

                    ],
            'dir' : self.mc_path,
            'sampleId' : 10,
            })

        self.QCD = self.makeSample({
            "name" : "QCD",
            "bins" :  [
                        'QCD_HT50to100',
                        'QCD_HT100to200',
                        'QCD_HT200to300',
                        'QCD_HT200to300_ext',
                        'QCD_HT300to500',
                        'QCD_HT300to500_ext',
                        'QCD_HT500to700',
                        'QCD_HT500to700_ext',
                        'QCD_HT700to1000',
                        'QCD_HT700to1000_ext',
                        'QCD_HT1000to1500',
                        'QCD_HT1000to1500_ext',
                        'QCD_HT1500to2000',
                        'QCD_HT1500to2000_ext',
                        'QCD_HT2000toInf',
                        'QCD_HT2000toInf_ext'

                ],
            'dir' : self.mc_path,
            'sampleId' : 30,

        })


        self.ZJetsHT = self.makeSample({
            "name" : "ZJetsHT",
            "bins" :  [
                       'ZJetsToNuNu_HT100to200',
                       'ZJetsToNuNu_HT100to200_ext',
                       'ZJetsToNuNu_HT200to400',
                       'ZJetsToNuNu_HT200to400_ext',
                       'ZJetsToNuNu_HT400to600',
                       'ZJetsToNuNu_HT400to600_ext',
                       'ZJetsToNuNu_HT600to800',
                       'ZJetsToNuNu_HT800to1200',
                       'ZJetsToNuNu_HT1200to2500',
                       'ZJetsToNuNu_HT1200to2500_ext',
                       'ZJetsToNuNu_HT2500toInf',

                      ] ,
            'dir' : self.mc_path ,
            'sampleId': 40,
            })


        self.DYJetsM5to50 = self.makeSample({
            "name" : "DYJetsM5to50",
            "bins" :  [
                       'DYJetsToLL_M5to50_HT100to200',
                       'DYJetsToLL_M5to50_HT100to200_ext',
                       'DYJetsToLL_M5to50_HT200to400',
                       'DYJetsToLL_M5to50_HT200to400_ext',
                       'DYJetsToLL_M5to50_HT400to600',
                       'DYJetsToLL_M5to50_HT600toInf',
                       'DYJetsToLL_M5to50_HT600toInf_ext',
                      ] ,
            'dir' : self.mc_path
            })


        self.DYJetsM50HT = self.makeSample({
            "name" : "DYJetsM50HT",
            "bins" :  [
                        "DYJetsToLL_M50_HT70to100"   ,
                        "DYJetsToLL_M50_HT100to200",
                        "DYJetsToLL_M50_HT100to200_ext",
                        "DYJetsToLL_M50_HT200to400",
                        "DYJetsToLL_M50_HT200to400_ext",
                        "DYJetsToLL_M50_HT400to600",
                        "DYJetsToLL_M50_HT400to600_ext",
                        "DYJetsToLL_M50_HT600to800"  ,
                        "DYJetsToLL_M50_HT800to1200" ,
                        "DYJetsToLL_M50_HT1200to2500",
                        "DYJetsToLL_M50_HT2500toInf" ,

                ] ,
            'dir' : self.mc_path,
            'sampleId': 50,
            })

        self.VV = self.makeSample({
        "name" : "VV",
        "bins" :  [
                   "WWTo2L2Nu",
                   "WWToLNuQQ",
                   "WWToLNuQQ_ext",
                   'WWTo1L1Nu2Q', #FIXME: Not used before?
    
                   "ZZTo2L2Nu",
                   "ZZTo2Q2Nu",
                   "ZZTo4L",
                   "ZZTo2L2Q",

                   "WZTo1L3Nu",
                   "WZTo1L1Nu2Q",
                   "WZTo2L2Q",
                   "WZTo3LNu", # FIXME: prblm?
                   ],
        'dir' : self.mc_path
        })

        self.ST = self.makeSample({
        "name" : "SingleTop",
        "bins" :  [
                   'T_tWch_ext',
                   'T_tch_powheg',
                   'TBar_tWch_ext',
                   'TBar_tch_powheg',
                  ] ,
        'dir' : self.mc_path
        })

        ######################################################################################################
        #####################################                  ###############################################
        #####################################       DATA       ###############################################
        #####################################                  ###############################################
        ######################################################################################################


        if getattr(self, "ichepdata"):
            dataSamples = [
                            ["MET",      ["MET_Run2016B-PromptReco-v2"           , "MET_Run2016C-PromptReco-v2"              ,  "MET_Run2016D-PromptReco-v2"            ]    ],
                            ["SingleMu", ["SingleMuon_Run2016B-PromptReco-v2"    , "SingleMuon_Run2016C-PromptReco-v2"       ,  "SingleMuon_Run2016D-PromptReco-v2"     ]    ],
                            ["SingleEl", ["SingleElectron_Run2016B-PromptReco-v2", "SingleElectron_Run2016C-PromptReco-v2"   ,  "SingleElectron_Run2016D-PromptReco-v2" ]    ],
                ]

        else:
            dataSamples = [\
                ['MET',      ["MET_Run2016B_03Feb2017_v2", "MET_Run2016D_03Feb2017", "MET_Run2016F_03Feb2017", "MET_Run2016H_03Feb2017_v2",
                              "MET_Run2016C_03Feb2017",    "MET_Run2016E_03Feb2017", "MET_Run2016G_03Feb2017", "MET_Run2016H_03Feb2017_v3"]],

                ['SingleEl', ["SingleElectron_Run2016B_03Feb2017_v2", "SingleElectron_Run2016D_03Feb2017", "SingleElectron_Run2016F_03Feb2017", "SingleElectron_Run2016H_03Feb2017_v2",
                              "SingleElectron_Run2016C_03Feb2017",    "SingleElectron_Run2016E_03Feb2017", "SingleElectron_Run2016G_03Feb2017", "SingleElectron_Run2016H_03Feb2017_v3"]],

                ['SingleMu', ["SingleMuon_Run2016B_03Feb2017_v2", "SingleMuon_Run2016D_03Feb2017", "SingleMuon_Run2016F_03Feb2017", "SingleMuon_Run2016H_03Feb2017_v2",
                              "SingleMuon_Run2016C_03Feb2017",    "SingleMuon_Run2016E_03Feb2017", "SingleMuon_Run2016G_03Feb2017", "SingleMuon_Run2016H_03Feb2017_v3"]],

                ['JetHT',    ["JetHT_Run2016B_03Feb2017_v2", "JetHT_Run2016D_03Feb2017", "JetHT_Run2016F_03Feb2017", "JetHT_Run2016H_03Feb2017_v2",
                              "JetHT_Run2016C_03Feb2017",    "JetHT_Run2016E_03Feb2017", "JetHT_Run2016G_03Feb2017", "JetHT_Run2016H_03Feb2017_v3"]],
            ]

        allData = []
        for data in dataSamples:
            sample = self.getDataSample(*data)
            setattr(self, data[0], sample)

        # signal samples

        allSignalStrings = [
            "T2DegStop_300_270",
            "T2DegStop_300_290_FastSim",
            "T2DegStop_300_270_FastSim",
            "T2DegStop_300_240_FastSim",
            "T2tt_300_270_FastSim",
            ]

        for s in allSignalStrings:
            sm = self.makeSample(self.getSignalSample(s))
            setattr(self, s, sm)


        signals_info = {
                             "SMS_T2tt_dM_10to80_genHT_160_genMET_80":              {'mass_template':'SMS_T2tt_mStop_%s_mLSP_%s',              'pkl':'SMS_T2tt_dM_10to80_genHT_160_genMET_80_mass_dict.pkl',               'scanId':1,   'shortName':'t2ttold%s_%s', 'niceName':'T2tt_%s_%s_mWMin5'},
                             "SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1":{'mass_template':'SMS_T2bW_X05_mStop_%s_mLSP_%s_mWMin0p1', 'pkl':'SMS_T2bW_X05_dM_10to80_genHT_160_genMET_80_mWMin_0p1_mass_dict.pkl', 'scanId':2,   'shortName':'t2bw%s_%s',    'niceName':'T2bW_%s_%s'},
                             "SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1":    {'mass_template':'SMS_T2tt_mStop_%s_mLSP_%s_mWMin0p1',     'pkl':'SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_mass_dict.pkl',     'scanId':3,   'shortName':'t2tt%s_%s',    'niceName':'T2tt_%s_%s'},
                             'SMS_TChiWZ_genHT_160_genMET_80':                      {'mass_template':'SMS_TChiWZ_Chipm2_%s_mLSP_%s',           'pkl':'SMS_TChiWZ_genHT_160_genMET_80_mass_dict.pkl',                       'scanId':4,   'shortName':'tchiwz%s_%s',  'niceName':'TChiWZ_%s_%s'},
                             'SMS_TChiWZ_genHT_160_genMET_80_3p':                   {'mass_template':'SMS_TChiWZ_Chipm2_%s_mLSP_%s',           'pkl':'SMS_TChiWZ_genHT_160_genMET_80_3p_mass_dict.pkl',                    'scanId':4,   'shortName':'tchiwz%s_%s',  'niceName':'TChiWZ_%s_%s'},
                             'MSSM_higgsino_genHT_160_genMET_80':                   {'mass_template':'MSSM_higgsino_mu_%s_M1_%s',              'pkl':'MSSM_higgsino_genHT_160_genMET_80_mass_dict.pkl',                    'scanId':5,   'shortName':'hino%s_%s',    'niceName':'Hino_%s_%s'},
                             'MSSM_higgsino_genHT_160_genMET_80_3p':                {'mass_template':'MSSM_higgsino_mu_%s_M1_%s',              'pkl':'MSSM_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',                 'scanId':5,   'shortName':'hino%s_%s',    'niceName':'Hino_%s_%s'},
                             'SMS_C1C1_higgsino_genHT_160_genMET_80_3p':            {'mass_template':'SMS_C1C1_mChipm1_%s_mLSP_%s',            'pkl':'SMS_C1C1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',             'scanId':123, 'shortName':'c1c1h%s_%s',   'niceName':'C1C1_%s_%s'},
                             'SMS_C1N1_higgsino_genHT_160_genMET_80_3p':            {'mass_template':'SMS_C1N1_mChipm1_%s_mLSP_%s',            'pkl':'SMS_C1N1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',             'scanId':123, 'shortName':'c1n1h%s_%s',   'niceName':'C1N1_%s_%s'},
                             'SMS_N2C1_higgsino_genHT_160_genMET_80_3p':            {'mass_template':'SMS_N2C1_mChi02_%s_mChipm01_%s',         'pkl':'SMS_N2C1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',             'scanId':123, 'shortName':'n2c1h%s_%s',   'niceName':'N2C1_%s_%s'},
                             'SMS_N2N1_higgsino_genHT_160_genMET_80_3p':            {'mass_template':'SMS_N2N1_mChi02_%s_mLSP_%s',             'pkl':'SMS_N2N1_higgsino_genHT_160_genMET_80_3p_mass_dict.pkl',             'scanId':123, 'shortName':'n2n1h%s_%s',   'niceName':'N2N1_%s_%s'},
                       }
  
        self.signals_info = signals_info
        
        cmgVersion = os.path.splitext(os.path.basename(__file__))[0].split('_')[2]
        cmg_MC_path =   'Workspace.DegenerateStopAnalysis.samples.cmgTuples.RunIISummer16MiniAODv2_%s'%cmgVersion
        cmg_MC = importlib.import_module(cmg_MC_path)
        cmg_sample_path = cmg_MC.sample_path

        for signal_name, signal_info in signals_info.items():
            mass_template            = signal_info['mass_template']
            scanId                   = signal_info['scanId']
            signal_mass_dict         = signal_info['pkl']
            
            mass_dict_path           = os.path.join(cmg_sample_path, "mass_dicts")
            mass_dict_pickle_file    = os.path.join(mass_dict_path, signal_mass_dict)
            signal_info['mass_dict'] = mass_dict_pickle_file 

            if os.path.isfile(mass_dict_pickle_file):
                mass_dict_pickle = mass_dict_pickle_file
                mass_dict        = pickle.load(open(mass_dict_pickle,"r"))
            else:
                print "!!!!! WARNING !!!!! NO MASS DICT FOUND! %s"%mass_dict_pickle_file
                print "!!!!! If no other fix available, enable useProxyMassDict and set mass_dict_pickle by hand!"
                mass_dict_pickle = None
                mass_dict        = {}

                useProxyMassDict = False
                if useProxyMassDict:
                    mass_dict_pickle = "/afs/hephy.at/data/nrad01/cmgTuples/postProcessed_mAODv2/8012_mAODv2_v3/80X_postProcessing_v10/analysisHephy_13TeV_2016_v0/step1/RunIISpring16MiniAODv2_v3/SMS_T2tt_dM_10to80_genHT_160_genMET_80_mass_dict.pkl"
                    mass_dict        = pickle.load(open(mass_dict_pickle,"r"))
                    print "!!!!!!!!!!! DOUBLE WARNING! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! USING PROXY MASS PICKLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
             
            mass_scan = {}

            for mstop in mass_dict:
                for mlsp in mass_dict[mstop]:
                    #mass_point = "SMS_T2tt_mStop_%s_mLSP_%s" % (mstop, mlsp)
                    mass_point = mass_template % (mstop, mlsp)
                    mass_scan[mass_point] = {
                        "name" : mass_point.replace(".","p"),
                        "bins": [mass_point.replace(".","p")],
                        'dir' : self.signal_path,
                        'sampleId': "%s%s%s" % (scanId, mstop, mlsp)
                        }


            for sig in mass_scan:
                sm = self.makeSample(mass_scan[sig])
                setattr(self, sig.replace(".","p"), sm)

if __name__=="__main__":
    cmgPP = cmgTuplesPostProcessed(mc_path, signal_path, data_path)
