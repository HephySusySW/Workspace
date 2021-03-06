sample_path_base = '/afs/hephy.at/data/nrad03/cmgTuples/'
sample_path_tag  = '/8025_mAODv2_v7_1/Data25ns' 

cache_file       = sample_path_base + sample_path_tag + "/data_cache.pkl" 
dpm_path         = '/dpm/oeaw.ac.at/home/cms/store/user/nrad/cmgTuples/' + sample_path_tag 


allComponents=[]

import os
if not os.path.isdir(sample_path_base + sample_path_tag):
    sample_path_base = '/data/nrad/cmgTuples/'
    if not os.path.isdir(sample_path_base + sample_path_tag):
        print "Cannot acces either afs-data or /data "
sample_path = sample_path_base + sample_path_tag


allComponents=[] 


JetHT_Run2016B_03Feb2017_v2 ={
'cmgName':"JetHT_Run2016B_03Feb2017_v2",
"name" : "JetHT_Run2016B-03Feb2017_ver2-v2",
"chunkString":"JetHT_Run2016B-03Feb2017_ver2-v2",
"dir": sample_path +"/" + "JetHT_Run2016B-03Feb2017_ver2-v2",
"dbsName" : "/JetHT/Run2016B-03Feb2017_ver2-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016B_03Feb2017_v2)

JetHT_Run2016B_23Sep2016 ={
'cmgName':"JetHT_Run2016B_23Sep2016",
"name" : "JetHT_Run2016B-23Sep2016-v3",
"chunkString":"JetHT_Run2016B-23Sep2016-v3",
"dir": sample_path +"/" + "JetHT_Run2016B-23Sep2016-v3",
"dbsName" : "/JetHT/Run2016B-23Sep2016-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016B_23Sep2016)



JetHT_Run2016C_03Feb2017 ={
'cmgName':"JetHT_Run2016C_03Feb2017",
"name" : "JetHT_Run2016C-03Feb2017-v1",
"chunkString":"JetHT_Run2016C-03Feb2017-v1",
"dir": sample_path +"/" + "JetHT_Run2016C-03Feb2017-v1",
"dbsName" : "/JetHT/Run2016C-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016C_03Feb2017)



JetHT_Run2016C_23Sep2016 ={
'cmgName':"JetHT_Run2016C_23Sep2016",
"name" : "JetHT_Run2016C-23Sep2016-v1",
"chunkString":"JetHT_Run2016C-23Sep2016-v1",
"dir": sample_path +"/" + "JetHT_Run2016C-23Sep2016-v1",
"dbsName" : "/JetHT/Run2016C-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016C_23Sep2016)



JetHT_Run2016D_03Feb2017 ={
'cmgName':"JetHT_Run2016D_03Feb2017",
"name" : "JetHT_Run2016D-03Feb2017-v1",
"chunkString":"JetHT_Run2016D-03Feb2017-v1",
"dir": sample_path +"/" + "JetHT_Run2016D-03Feb2017-v1",
"dbsName" : "/JetHT/Run2016D-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016D_03Feb2017)



JetHT_Run2016D_23Sep2016 ={
'cmgName':"JetHT_Run2016D_23Sep2016",
"name" : "JetHT_Run2016D-23Sep2016-v1",
"chunkString":"JetHT_Run2016D-23Sep2016-v1",
"dir": sample_path +"/" + "JetHT_Run2016D-23Sep2016-v1",
"dbsName" : "/JetHT/Run2016D-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016D_23Sep2016)



JetHT_Run2016E_03Feb2017 ={
'cmgName':"JetHT_Run2016E_03Feb2017",
"name" : "JetHT_Run2016E-03Feb2017-v1",
"chunkString":"JetHT_Run2016E-03Feb2017-v1",
"dir": sample_path +"/" + "JetHT_Run2016E-03Feb2017-v1",
"dbsName" : "/JetHT/Run2016E-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016E_03Feb2017)



JetHT_Run2016E_23Sep2016 ={
'cmgName':"JetHT_Run2016E_23Sep2016",
"name" : "JetHT_Run2016E-23Sep2016-v1",
"chunkString":"JetHT_Run2016E-23Sep2016-v1",
"dir": sample_path +"/" + "JetHT_Run2016E-23Sep2016-v1",
"dbsName" : "/JetHT/Run2016E-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016E_23Sep2016)



JetHT_Run2016F_03Feb2017 ={
'cmgName':"JetHT_Run2016F_03Feb2017",
"name" : "JetHT_Run2016F-03Feb2017-v1",
"chunkString":"JetHT_Run2016F-03Feb2017-v1",
"dir": sample_path +"/" + "JetHT_Run2016F-03Feb2017-v1",
"dbsName" : "/JetHT/Run2016F-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016F_03Feb2017)



JetHT_Run2016F_23Sep2016 ={
'cmgName':"JetHT_Run2016F_23Sep2016",
"name" : "JetHT_Run2016F-23Sep2016-v1",
"chunkString":"JetHT_Run2016F-23Sep2016-v1",
"dir": sample_path +"/" + "JetHT_Run2016F-23Sep2016-v1",
"dbsName" : "/JetHT/Run2016F-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016F_23Sep2016)



JetHT_Run2016G_03Feb2017 ={
'cmgName':"JetHT_Run2016G_03Feb2017",
"name" : "JetHT_Run2016G-03Feb2017-v1",
"chunkString":"JetHT_Run2016G-03Feb2017-v1",
"dir": sample_path +"/" + "JetHT_Run2016G-03Feb2017-v1",
"dbsName" : "/JetHT/Run2016G-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016G_03Feb2017)



JetHT_Run2016G_23Sep2016 ={
'cmgName':"JetHT_Run2016G_23Sep2016",
"name" : "JetHT_Run2016G-23Sep2016-v1",
"chunkString":"JetHT_Run2016G-23Sep2016-v1",
"dir": sample_path +"/" + "JetHT_Run2016G-23Sep2016-v1",
"dbsName" : "/JetHT/Run2016G-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016G_23Sep2016)



JetHT_Run2016H_03Feb2017_v2 ={
'cmgName':"JetHT_Run2016H_03Feb2017_v2",
"name" : "JetHT_Run2016H-03Feb2017_ver2-v1",
"chunkString":"JetHT_Run2016H-03Feb2017_ver2-v1",
"dir": sample_path +"/" + "JetHT_Run2016H-03Feb2017_ver2-v1",
"dbsName" : "/JetHT/Run2016H-03Feb2017_ver2-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016H_03Feb2017_v2)



JetHT_Run2016H_03Feb2017_v3 ={
'cmgName':"JetHT_Run2016H_03Feb2017_v3",
"name" : "JetHT_Run2016H-03Feb2017_ver3-v1",
"chunkString":"JetHT_Run2016H-03Feb2017_ver3-v1",
"dir": sample_path +"/" + "JetHT_Run2016H-03Feb2017_ver3-v1",
"dbsName" : "/JetHT/Run2016H-03Feb2017_ver3-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016H_03Feb2017_v3)



JetHT_Run2016H_PromptReco_v2 ={
'cmgName':"JetHT_Run2016H_PromptReco_v2",
"name" : "JetHT_Run2016H-PromptReco-v2",
"chunkString":"JetHT_Run2016H-PromptReco-v2",
"dir": sample_path +"/" + "JetHT_Run2016H-PromptReco-v2",
"dbsName" : "/JetHT/Run2016H-PromptReco-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016H_PromptReco_v2)



JetHT_Run2016H_PromptReco_v3 ={
'cmgName':"JetHT_Run2016H_PromptReco_v3",
"name" : "JetHT_Run2016H-PromptReco-v3",
"chunkString":"JetHT_Run2016H-PromptReco-v3",
"dir": sample_path +"/" + "JetHT_Run2016H-PromptReco-v3",
"dbsName" : "/JetHT/Run2016H-PromptReco-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(JetHT_Run2016H_PromptReco_v3)



MET_Run2016B_03Feb2017_v2 ={
'cmgName':"MET_Run2016B_03Feb2017_v2",
"name" : "MET_Run2016B-03Feb2017_ver2-v2",
"chunkString":"MET_Run2016B-03Feb2017_ver2-v2",
"dir": sample_path +"/" + "MET_Run2016B-03Feb2017_ver2-v2",
"dbsName" : "/MET/Run2016B-03Feb2017_ver2-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016B_03Feb2017_v2)



MET_Run2016B_23Sep2016 ={
'cmgName':"MET_Run2016B_23Sep2016",
"name" : "MET_Run2016B-23Sep2016-v3",
"chunkString":"MET_Run2016B-23Sep2016-v3",
"dir": sample_path +"/" + "MET_Run2016B-23Sep2016-v3",
"dbsName" : "/MET/Run2016B-23Sep2016-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016B_23Sep2016)



MET_Run2016C_03Feb2017 ={
'cmgName':"MET_Run2016C_03Feb2017",
"name" : "MET_Run2016C-03Feb2017-v1",
"chunkString":"MET_Run2016C-03Feb2017-v1",
"dir": sample_path +"/" + "MET_Run2016C-03Feb2017-v1",
"dbsName" : "/MET/Run2016C-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016C_03Feb2017)



MET_Run2016C_23Sep2016 ={
'cmgName':"MET_Run2016C_23Sep2016",
"name" : "MET_Run2016C-23Sep2016-v1",
"chunkString":"MET_Run2016C-23Sep2016-v1",
"dir": sample_path +"/" + "MET_Run2016C-23Sep2016-v1",
"dbsName" : "/MET/Run2016C-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016C_23Sep2016)



MET_Run2016D_03Feb2017 ={
'cmgName':"MET_Run2016D_03Feb2017",
"name" : "MET_Run2016D-03Feb2017-v1",
"chunkString":"MET_Run2016D-03Feb2017-v1",
"dir": sample_path +"/" + "MET_Run2016D-03Feb2017-v1",
"dbsName" : "/MET/Run2016D-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016D_03Feb2017)



MET_Run2016D_23Sep2016 ={
'cmgName':"MET_Run2016D_23Sep2016",
"name" : "MET_Run2016D-23Sep2016-v1",
"chunkString":"MET_Run2016D-23Sep2016-v1",
"dir": sample_path +"/" + "MET_Run2016D-23Sep2016-v1",
"dbsName" : "/MET/Run2016D-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016D_23Sep2016)



MET_Run2016E_03Feb2017 ={
'cmgName':"MET_Run2016E_03Feb2017",
"name" : "MET_Run2016E-03Feb2017-v1",
"chunkString":"MET_Run2016E-03Feb2017-v1",
"dir": sample_path +"/" + "MET_Run2016E-03Feb2017-v1",
"dbsName" : "/MET/Run2016E-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016E_03Feb2017)



MET_Run2016E_23Sep2016 ={
'cmgName':"MET_Run2016E_23Sep2016",
"name" : "MET_Run2016E-23Sep2016-v1",
"chunkString":"MET_Run2016E-23Sep2016-v1",
"dir": sample_path +"/" + "MET_Run2016E-23Sep2016-v1",
"dbsName" : "/MET/Run2016E-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016E_23Sep2016)



MET_Run2016F_03Feb2017 ={
'cmgName':"MET_Run2016F_03Feb2017",
"name" : "MET_Run2016F-03Feb2017-v1",
"chunkString":"MET_Run2016F-03Feb2017-v1",
"dir": sample_path +"/" + "MET_Run2016F-03Feb2017-v1",
"dbsName" : "/MET/Run2016F-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016F_03Feb2017)



MET_Run2016F_23Sep2016 ={
'cmgName':"MET_Run2016F_23Sep2016",
"name" : "MET_Run2016F-23Sep2016-v1",
"chunkString":"MET_Run2016F-23Sep2016-v1",
"dir": sample_path +"/" + "MET_Run2016F-23Sep2016-v1",
"dbsName" : "/MET/Run2016F-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016F_23Sep2016)



MET_Run2016G_03Feb2017 ={
'cmgName':"MET_Run2016G_03Feb2017",
"name" : "MET_Run2016G-03Feb2017-v1",
"chunkString":"MET_Run2016G-03Feb2017-v1",
"dir": sample_path +"/" + "MET_Run2016G-03Feb2017-v1",
"dbsName" : "/MET/Run2016G-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016G_03Feb2017)



MET_Run2016G_23Sep2016 ={
'cmgName':"MET_Run2016G_23Sep2016",
"name" : "MET_Run2016G-23Sep2016-v1",
"chunkString":"MET_Run2016G-23Sep2016-v1",
"dir": sample_path +"/" + "MET_Run2016G-23Sep2016-v1",
"dbsName" : "/MET/Run2016G-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016G_23Sep2016)



MET_Run2016H_03Feb2017_v2 ={
'cmgName':"MET_Run2016H_03Feb2017_v2",
"name" : "MET_Run2016H-03Feb2017_ver2-v1",
"chunkString":"MET_Run2016H-03Feb2017_ver2-v1",
"dir": sample_path +"/" + "MET_Run2016H-03Feb2017_ver2-v1",
"dbsName" : "/MET/Run2016H-03Feb2017_ver2-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016H_03Feb2017_v2)



MET_Run2016H_03Feb2017_v3 ={
'cmgName':"MET_Run2016H_03Feb2017_v3",
"name" : "MET_Run2016H-03Feb2017_ver3-v1",
"chunkString":"MET_Run2016H-03Feb2017_ver3-v1",
"dir": sample_path +"/" + "MET_Run2016H-03Feb2017_ver3-v1",
"dbsName" : "/MET/Run2016H-03Feb2017_ver3-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016H_03Feb2017_v3)



MET_Run2016H_PromptReco_v2 ={
'cmgName':"MET_Run2016H_PromptReco_v2",
"name" : "MET_Run2016H-PromptReco-v2",
"chunkString":"MET_Run2016H-PromptReco-v2",
"dir": sample_path +"/" + "MET_Run2016H-PromptReco-v2",
"dbsName" : "/MET/Run2016H-PromptReco-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016H_PromptReco_v2)



MET_Run2016H_PromptReco_v3 ={
'cmgName':"MET_Run2016H_PromptReco_v3",
"name" : "MET_Run2016H-PromptReco-v3",
"chunkString":"MET_Run2016H-PromptReco-v3",
"dir": sample_path +"/" + "MET_Run2016H-PromptReco-v3",
"dbsName" : "/MET/Run2016H-PromptReco-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(MET_Run2016H_PromptReco_v3)



SingleElectron_Run2016B_03Feb2017_v2 ={
'cmgName':"SingleElectron_Run2016B_03Feb2017_v2",
"name" : "SingleElectron_Run2016B-03Feb2017_ver2-v2",
"chunkString":"SingleElectron_Run2016B-03Feb2017_ver2-v2",
"dir": sample_path +"/" + "SingleElectron_Run2016B-03Feb2017_ver2-v2",
"dbsName" : "/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016B_03Feb2017_v2)



SingleElectron_Run2016B_23Sep2016 ={
'cmgName':"SingleElectron_Run2016B_23Sep2016",
"name" : "SingleElectron_Run2016B-23Sep2016-v3",
"chunkString":"SingleElectron_Run2016B-23Sep2016-v3",
"dir": sample_path +"/" + "SingleElectron_Run2016B-23Sep2016-v3",
"dbsName" : "/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016B_23Sep2016)



SingleElectron_Run2016C_03Feb2017 ={
'cmgName':"SingleElectron_Run2016C_03Feb2017",
"name" : "SingleElectron_Run2016C-03Feb2017-v1",
"chunkString":"SingleElectron_Run2016C-03Feb2017-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016C-03Feb2017-v1",
"dbsName" : "/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016C_03Feb2017)



SingleElectron_Run2016C_23Sep2016 ={
'cmgName':"SingleElectron_Run2016C_23Sep2016",
"name" : "SingleElectron_Run2016C-23Sep2016-v1",
"chunkString":"SingleElectron_Run2016C-23Sep2016-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016C-23Sep2016-v1",
"dbsName" : "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016C_23Sep2016)



SingleElectron_Run2016D_03Feb2017 ={
'cmgName':"SingleElectron_Run2016D_03Feb2017",
"name" : "SingleElectron_Run2016D-03Feb2017-v1",
"chunkString":"SingleElectron_Run2016D-03Feb2017-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016D-03Feb2017-v1",
"dbsName" : "/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016D_03Feb2017)



SingleElectron_Run2016D_23Sep2016 ={
'cmgName':"SingleElectron_Run2016D_23Sep2016",
"name" : "SingleElectron_Run2016D-23Sep2016-v1",
"chunkString":"SingleElectron_Run2016D-23Sep2016-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016D-23Sep2016-v1",
"dbsName" : "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016D_23Sep2016)



SingleElectron_Run2016E_03Feb2017 ={
'cmgName':"SingleElectron_Run2016E_03Feb2017",
"name" : "SingleElectron_Run2016E-03Feb2017-v1",
"chunkString":"SingleElectron_Run2016E-03Feb2017-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016E-03Feb2017-v1",
"dbsName" : "/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016E_03Feb2017)



SingleElectron_Run2016E_23Sep2016 ={
'cmgName':"SingleElectron_Run2016E_23Sep2016",
"name" : "SingleElectron_Run2016E-23Sep2016-v1",
"chunkString":"SingleElectron_Run2016E-23Sep2016-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016E-23Sep2016-v1",
"dbsName" : "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016E_23Sep2016)



SingleElectron_Run2016F_03Feb2017 ={
'cmgName':"SingleElectron_Run2016F_03Feb2017",
"name" : "SingleElectron_Run2016F-03Feb2017-v1",
"chunkString":"SingleElectron_Run2016F-03Feb2017-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016F-03Feb2017-v1",
"dbsName" : "/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016F_03Feb2017)



SingleElectron_Run2016F_23Sep2016 ={
'cmgName':"SingleElectron_Run2016F_23Sep2016",
"name" : "SingleElectron_Run2016F-23Sep2016-v1",
"chunkString":"SingleElectron_Run2016F-23Sep2016-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016F-23Sep2016-v1",
"dbsName" : "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016F_23Sep2016)



SingleElectron_Run2016G_03Feb2017 ={
'cmgName':"SingleElectron_Run2016G_03Feb2017",
"name" : "SingleElectron_Run2016G-03Feb2017-v1",
"chunkString":"SingleElectron_Run2016G-03Feb2017-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016G-03Feb2017-v1",
"dbsName" : "/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016G_03Feb2017)



SingleElectron_Run2016G_23Sep2016 ={
'cmgName':"SingleElectron_Run2016G_23Sep2016",
"name" : "SingleElectron_Run2016G-23Sep2016-v1",
"chunkString":"SingleElectron_Run2016G-23Sep2016-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016G-23Sep2016-v1",
"dbsName" : "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016G_23Sep2016)



SingleElectron_Run2016H_03Feb2017_v2 ={
'cmgName':"SingleElectron_Run2016H_03Feb2017_v2",
"name" : "SingleElectron_Run2016H-03Feb2017_ver2-v1",
"chunkString":"SingleElectron_Run2016H-03Feb2017_ver2-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016H-03Feb2017_ver2-v1",
"dbsName" : "/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016H_03Feb2017_v2)



SingleElectron_Run2016H_03Feb2017_v3 ={
'cmgName':"SingleElectron_Run2016H_03Feb2017_v3",
"name" : "SingleElectron_Run2016H-03Feb2017_ver3-v1",
"chunkString":"SingleElectron_Run2016H-03Feb2017_ver3-v1",
"dir": sample_path +"/" + "SingleElectron_Run2016H-03Feb2017_ver3-v1",
"dbsName" : "/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016H_03Feb2017_v3)



SingleElectron_Run2016H_PromptReco_v2 ={
'cmgName':"SingleElectron_Run2016H_PromptReco_v2",
"name" : "SingleElectron_Run2016H-PromptReco-v2",
"chunkString":"SingleElectron_Run2016H-PromptReco-v2",
"dir": sample_path +"/" + "SingleElectron_Run2016H-PromptReco-v2",
"dbsName" : "/SingleElectron/Run2016H-PromptReco-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016H_PromptReco_v2)



SingleElectron_Run2016H_PromptReco_v3 ={
'cmgName':"SingleElectron_Run2016H_PromptReco_v3",
"name" : "SingleElectron_Run2016H-PromptReco-v3",
"chunkString":"SingleElectron_Run2016H-PromptReco-v3",
"dir": sample_path +"/" + "SingleElectron_Run2016H-PromptReco-v3",
"dbsName" : "/SingleElectron/Run2016H-PromptReco-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleElectron_Run2016H_PromptReco_v3)



SingleMuon_Run2016B_03Feb2017_v2 ={
'cmgName':"SingleMuon_Run2016B_03Feb2017_v2",
"name" : "SingleMuon_Run2016B-03Feb2017_ver2-v2",
"chunkString":"SingleMuon_Run2016B-03Feb2017_ver2-v2",
"dir": sample_path +"/" + "SingleMuon_Run2016B-03Feb2017_ver2-v2",
"dbsName" : "/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016B_03Feb2017_v2)



SingleMuon_Run2016B_23Sep2016 ={
'cmgName':"SingleMuon_Run2016B_23Sep2016",
"name" : "SingleMuon_Run2016B-23Sep2016-v3",
"chunkString":"SingleMuon_Run2016B-23Sep2016-v3",
"dir": sample_path +"/" + "SingleMuon_Run2016B-23Sep2016-v3",
"dbsName" : "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016B_23Sep2016)



SingleMuon_Run2016C_03Feb2017 ={
'cmgName':"SingleMuon_Run2016C_03Feb2017",
"name" : "SingleMuon_Run2016C-03Feb2017-v1",
"chunkString":"SingleMuon_Run2016C-03Feb2017-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016C-03Feb2017-v1",
"dbsName" : "/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016C_03Feb2017)



SingleMuon_Run2016C_23Sep2016 ={
'cmgName':"SingleMuon_Run2016C_23Sep2016",
"name" : "SingleMuon_Run2016C-23Sep2016-v1",
"chunkString":"SingleMuon_Run2016C-23Sep2016-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016C-23Sep2016-v1",
"dbsName" : "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016C_23Sep2016)



SingleMuon_Run2016D_03Feb2017 ={
'cmgName':"SingleMuon_Run2016D_03Feb2017",
"name" : "SingleMuon_Run2016D-03Feb2017-v1",
"chunkString":"SingleMuon_Run2016D-03Feb2017-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016D-03Feb2017-v1",
"dbsName" : "/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016D_03Feb2017)



SingleMuon_Run2016D_23Sep2016 ={
'cmgName':"SingleMuon_Run2016D_23Sep2016",
"name" : "SingleMuon_Run2016D-23Sep2016-v1",
"chunkString":"SingleMuon_Run2016D-23Sep2016-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016D-23Sep2016-v1",
"dbsName" : "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016D_23Sep2016)



SingleMuon_Run2016E_03Feb2017 ={
'cmgName':"SingleMuon_Run2016E_03Feb2017",
"name" : "SingleMuon_Run2016E-03Feb2017-v1",
"chunkString":"SingleMuon_Run2016E-03Feb2017-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016E-03Feb2017-v1",
"dbsName" : "/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016E_03Feb2017)



SingleMuon_Run2016E_23Sep2016 ={
'cmgName':"SingleMuon_Run2016E_23Sep2016",
"name" : "SingleMuon_Run2016E-23Sep2016-v1",
"chunkString":"SingleMuon_Run2016E-23Sep2016-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016E-23Sep2016-v1",
"dbsName" : "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016E_23Sep2016)



SingleMuon_Run2016F_03Feb2017 ={
'cmgName':"SingleMuon_Run2016F_03Feb2017",
"name" : "SingleMuon_Run2016F-03Feb2017-v1",
"chunkString":"SingleMuon_Run2016F-03Feb2017-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016F-03Feb2017-v1",
"dbsName" : "/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016F_03Feb2017)



SingleMuon_Run2016F_23Sep2016 ={
'cmgName':"SingleMuon_Run2016F_23Sep2016",
"name" : "SingleMuon_Run2016F-23Sep2016-v1",
"chunkString":"SingleMuon_Run2016F-23Sep2016-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016F-23Sep2016-v1",
"dbsName" : "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016F_23Sep2016)



SingleMuon_Run2016G_03Feb2017 ={
'cmgName':"SingleMuon_Run2016G_03Feb2017",
"name" : "SingleMuon_Run2016G-03Feb2017-v1",
"chunkString":"SingleMuon_Run2016G-03Feb2017-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016G-03Feb2017-v1",
"dbsName" : "/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016G_03Feb2017)



SingleMuon_Run2016G_23Sep2016 ={
'cmgName':"SingleMuon_Run2016G_23Sep2016",
"name" : "SingleMuon_Run2016G-23Sep2016-v1",
"chunkString":"SingleMuon_Run2016G-23Sep2016-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016G-23Sep2016-v1",
"dbsName" : "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016G_23Sep2016)



SingleMuon_Run2016H_03Feb2017_v2 ={
'cmgName':"SingleMuon_Run2016H_03Feb2017_v2",
"name" : "SingleMuon_Run2016H-03Feb2017_ver2-v1",
"chunkString":"SingleMuon_Run2016H-03Feb2017_ver2-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016H-03Feb2017_ver2-v1",
"dbsName" : "/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016H_03Feb2017_v2)



SingleMuon_Run2016H_03Feb2017_v3 ={
'cmgName':"SingleMuon_Run2016H_03Feb2017_v3",
"name" : "SingleMuon_Run2016H-03Feb2017_ver3-v1",
"chunkString":"SingleMuon_Run2016H-03Feb2017_ver3-v1",
"dir": sample_path +"/" + "SingleMuon_Run2016H-03Feb2017_ver3-v1",
"dbsName" : "/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016H_03Feb2017_v3)



SingleMuon_Run2016H_PromptReco_v2 ={
'cmgName':"SingleMuon_Run2016H_PromptReco_v2",
"name" : "SingleMuon_Run2016H-PromptReco-v2",
"chunkString":"SingleMuon_Run2016H-PromptReco-v2",
"dir": sample_path +"/" + "SingleMuon_Run2016H-PromptReco-v2",
"dbsName" : "/SingleMuon/Run2016H-PromptReco-v2/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016H_PromptReco_v2)



SingleMuon_Run2016H_PromptReco_v3 ={
'cmgName':"SingleMuon_Run2016H_PromptReco_v3",
"name" : "SingleMuon_Run2016H-PromptReco-v3",
"chunkString":"SingleMuon_Run2016H-PromptReco-v3",
"dir": sample_path +"/" + "SingleMuon_Run2016H-PromptReco-v3",
"dbsName" : "/SingleMuon/Run2016H-PromptReco-v3/MINIAOD",
"rootFileLocation":"tree.root",
"skimAnalyzerDir":"skimAnalyzerCount",
"treeName":"tree",
"isData": True,
"xsec": None,


}
allComponents.append(SingleMuon_Run2016H_PromptReco_v3)





def getHeppyMap():
    from Workspace.DegenerateStopAnalysis.samples.heppy_dpm_samples import heppy_mapper
    heppy_samples = heppy_mapper( allComponents, [dpm_path], cache_file )
    return heppy_samples 
