import re
import math
import copy
import collections

from Workspace.DegenerateStopAnalysis.samples.baselineSamplesInfo import cutWeightOptions
from Workspace.DegenerateStopAnalysis.tools.degTools import CutClass, joinCutStrings, splitCutInPt, btw, less, more
from Workspace.DegenerateStopAnalysis.tools.degVars  import VarsCutsWeightsRegions
from Workspace.DegenerateStopAnalysis.tools.degTools import getSampleTriggersFilters

#from Workspace.DegenerateStopAnalysis.tools.btag_sf_map import BTagSFMap 
#import Workspace.DegenerateStopAnalysis.tools.degWeights as degWeights

class Variable(object):
    def __init__(self, name, string, latex=None):
        self.name   = name
        self.string = str(string)
        self.latex  = latex if latex else ''
    def __str__(self):
        return self.string
    def __repr__(self):
        return "<%s.%s %s: %s >"%(self.__module__, self.__class__.__name__, self.name, self.string)

class Variables():
    def __init__( self, vars_dict = None , verbose = False):
        self.vars_dict_orig   = copy.deepcopy(vars_dict)
        self.verbose = verbose 
        #self.format_vars_dict()
        self._update()

    def _update(self):
        self.format_vars_dict()

    def format_vars_dict( self ):
        """ formats the vars_dict for variables that depend on other variables , i.e. LepIndex, etc. can be done in a smarter way.  """
        self.vars_dict_format = { varName: varInfo['var'] for varName, varInfo in self.vars_dict_orig.iteritems() }
        #print self.vars_dict_format 
        self.vars_dict   = copy.deepcopy(self.vars_dict_orig)
        for varName, varInfo in self.vars_dict.items():
            #print varInfo['var']
            varFormatMaxDepth = 5
            varFormatDepth = 0
            varInfo['var'] = str(varInfo['var'])
            while re.search(r'{(.*?)}',varInfo['var'] ) and varFormatDepth < varFormatMaxDepth: 
                varInfo['var']  = varInfo['var'].format(**self.vars_dict_format)
                varFormatDepth += 1
                #print varInfo['var']
                #print varFormatDepth
            setattr(self, varName, Variable( varName, varInfo['var'], varInfo['latex'])) 
        self.vars_dict_format = { varName: varInfo['var'] for varName, varInfo in self.vars_dict.iteritems() } 

def isDataSample(sample):
    isDataSample_ = False
    if isSampleInst(sample):
        isDataSample_ = sample.isData
    else:
        dataSampleNames  = ['data', 'dblind', 'dunblind', 'dichep' ]
        if getattr( sample, "isData", ""):
            pass #isDataSample_ = True
        elif type(sample)==str:
            if any([dataSampleName in sample.lower() for dataSampleName in dataSampleNames]):
                isDataSample_ = True
    return isDataSample_ 


def isSampleInst(sample):
    isSampleInst_ = False
    if hasattr(sample, 'name') :
        isSampleInst_ = True
    return isSampleInst_
    #if type(sample)==type(""):
    #    sampleName = sample
    #elif hasattr(sample, "name"):
    #    sampleName = sample.name
    #    sampleInst = sample
    #elif type(sample) == type({}) and sample.has_key('name'):
    #    sampleName = sample['name']
    #else:
    #    raise Exception("sample type is not recognized %s"%sample)
    #return samplename, sampleInst


class Weights(Variables):
    def combine( self, weightList):
        #weights_to_combine = [ getattr(self.weights,wname) for wname in weightList]
        weights_to_combine = [ getattr(self,wname) for wname in weightList]
        return '*'.join(['(%s)'%w for w in weights_to_combine])

    def _makeCutWeightOptFunc( self, sample_list, weight_options, cut_options):
        """
        Create a function to add weights based on sample name and cut
        """
        verbose = False
        def cutWeightOptFunc(sample, cutListNames, weightListNames):

            isSampleInst_ =  isSampleInst(sample)
            sampleName    =  sample.name if isSampleInst_ else sample 
            if verbose:
                print "---cutWeightOptFunc"
                print "samp:" , sampleName 
                print "cutListNames", cutListNames
                print "weightListNames", weightListNames
                print "options:", weight_options, cut_options 
            if isDataSample( sample ):
                
                #return sample, cutListNames, weightListNames
                if not (sample_list and hasattr(sample_list, '__call__') and sample_list(sample) ):
                    if verbose: print "isData: Opt doesn't apply to sample", sampleName
                    return sample, cutListNames, ["noweight"]
                else:
                    print "Extra Cut/Weight for data, are you sure? %s,%s"%(cutListNames, weightListNames)
            #if sample_list and hasattr(sample_list, "__cal__") and not sample_list(sample): #sample not in sample_list:
            #cutListNames
            if sample_list and hasattr(sample_list, "__call__"): #sample not in sample_list:
                if not isSampleInst_:
                    raise Exception("The weight/cut option (%s, %s) has a function for selecting the sample, \n \
                                     but a sample string name (%s) is passed to the getSampleCutWeight probably, \n \
                                     what should we do here?"%(weight_options , cut_options, sample) )
                #print sample_list, weight_options
                #print sample.name
                #print sample_list(sample)
                if not sample_list(sample) :
                    if verbose:
                        print "Sample Func: Opt doesn't apply to sample", sampleName
                    return sample, cutListNames, weightListNames
            elif sample_list and type(sample_list)==type([]) and not any([x in sampleName for x in sample_list]): #sample not in sample_list:
                #print "sample not in sample_list : ", sample_list
                if verbose: print "Sample List: Opt doesn't apply to sample", sampleName
                return sample, cutListNames, weightListNames
            
            if weight_options:
                options = [x for x in weight_options if not x == "default"]
                new_weights = []
                if verbose: print "weight options", options 
                for cut in options:
                    if cut in cutListNames:
                        new_weights.append(weight_options[cut])
                        #cutListNames.remove(cut) # should or shouldn't remove cut? if remove can cause problems for cut dependent weights 
                if len(new_weights)>1:
                    assert False, ["Seems like more than one option was applicable....", cutListNames, weight_options, new_weights]
                if not new_weights:
                    if weight_options.get("default"):
                        new_weights.append( weight_options["default"])
                weightListNames.extend(new_weights)
                for w in new_weights:
                    if w in cutListNames:
                        if verbose: print w, "removed from cutList! %s"%cutListNames , "for", sample
                        cutListNames.pop(cutListNames.index(w))
                if verbose: print sampleName, cutListNames, weightListNames
            if cut_options:
                options = [x for x in cut_options if not x == "default"]
                new_cuts = []
                if verbose: print "cut options", options 
                for cut in options:
                    if cut in cutListNames:   ## Add the 
                        
                        new_cuts.extend(cut_options[cut])
                        #cutListNames.remove(cut) ## remove cut from cutList, also if the weight is in the cutList it will be removed
                if len(new_cuts)>1:
                    assert False, ["Seems like more than one option was applicable....", cutListNames, cut_options, new_cuts]
                if not new_cuts:
                    if cut_options.get("default"):
                        new_cuts.append( cut_options["default"])
                cutListNames.extend(new_cuts)
                #for c in new_cuts:
                #    if c in cutListNames:
                #        #print w, "removed from cutList! %s"%cutListNames , "for", sample
                #        cutListNames.pop(cutListNames.index(w))
                if verbose: print sampleName, cutListNames, weightListNames
            return sample, cutListNames, weightListNames
        setattr( cutWeightOptFunc, "weight_options", weight_options)
        setattr( cutWeightOptFunc, "cut_options", cut_options)
        setattr( cutWeightOptFunc, "sample_list", sample_list)
        return cutWeightOptFunc

    def _makeCutWeightFuncs(self,  cut_weight_options):
        self.cut_weight_funcs = {}
        for cut_weight_option_name, cut_weight_option in cut_weight_options.items():
            if self.verbose :  print cut_weight_option_name, cut_weight_option
            self.cut_weight_funcs[cut_weight_option_name] = self._makeCutWeightOptFunc( cut_weight_option['sample_list'], cut_weight_option.get('weight_options') , cut_weight_option.get("cut_options")  )
            ### Here I change the name of the func and add it to make it picklable..... a better solution?
            funcname = "cutWeightOptFunc_"+cut_weight_option_name
            self.cut_weight_funcs[cut_weight_option_name].__name__ = funcname


class Cuts():
    #def __init__( self, settings =None, cuts_dict = None , vars={}, regions ={}, weights = None, def_weights = None,options=None):
    def __init__( self, settings =None, def_weights = ["weight"], options=[], alternative_vars = {}):
        self.def_weights = def_weights
        self.options     = options
        self.settings    = settings
        self.alternative_vars = alternative_vars
        self._update()
    def _evaluateInput(self):
        if self.settings:
            print self.settings
            varsCutsWeightsRegions = VarsCutsWeightsRegions(**self.settings)
            weights_dict           = varsCutsWeightsRegions.weights_dict
            cut_weight_options         = varsCutsWeightsRegions.cut_weight_options
            regions                = varsCutsWeightsRegions.regions
            cuts_dict              = varsCutsWeightsRegions.cuts_dict
            weights                = Weights(weights_dict)
            weights._makeCutWeightFuncs(cut_weight_options)
            self.weights     = weights
            vars                   = varsCutsWeightsRegions.vars_dict
            if self.alternative_vars:
                vars.update(self.alternative_vars)
            vars=Variables(vars)

            self.varsCutsWeightsRegions = varsCutsWeightsRegions
        else:
            pass
        if type(vars)==dict:
            vars = Variables(vars)
        if not getattr(vars, "vars_dict"):
            raise Exception("Variables must be from Variable Class or a dictionary of variables but it was: %s"%(vars))
        self.vars        =  vars
        self.vars_dict_format = vars.vars_dict_format
        self.cuts_dict_orig   = copy.deepcopy(cuts_dict)
        #self.cuts_dict   = cuts_dict
        self.cutInstList = []
        self.cutInsts    = {}
        self.regions     = regions
        
    def _reset(self):
        self._evaluateInput()


    def _update(self, reset = True):
        if reset:
            self._reset()
        self.vars._update()
        self.weights._update()
        self.vars_dict_format = self.vars.vars_dict_format
        self._format_cuts_dict()
        self._makeRegions(self.regions)
    def _format_cuts_dict( self ):
        #self.vars_dict_format = { varName: varInfo['var'] for varName, varInfo in self.cuts_dict.iteritems() }
        self.cuts_dict = copy.deepcopy( self.cuts_dict_orig )
        for cutName, cutInfo in self.cuts_dict.items():
            cutInfo['cut'] = cutInfo['cut'].format(**self.vars_dict_format)

    def _makeRegions(self, regions):
        for region_name, region_info in regions.iteritems():
            cutLists = []
            if region_info.has_key("regions"):
                cutList = [ [subregion, getattr(self, subregion).combined] for subregion in region_info['regions'] ]
                cutLists.extend(cutList)  
            if region_info.has_key("cuts"):
                cutListNames = region_info['cuts']
                cutList      = [ [cutName, self.cuts_dict[cutName]['cut']] for cutName in cutListNames]
                cutLists.extend(cutList)
                #self._makeCutClass(region_name, cutListNames = region_info['cuts'], baseCut = region_info['baseCut'])
            if cutLists :
                #print region_name , cutLists
                self._makeCutClass( region_name, cutList = cutLists, baseCut = region_info['baseCut'] )

    def _makeCutClass( self, name, cutListNames=None , baseCut =None, cutList = None, update = True):
        #print 'making cut class', name
        if cutListNames:
            cutList = [ [cutName, self.cuts_dict[cutName]['cut']] for cutName in cutListNames]
        elif cutList:
            pass
        if type(baseCut)==type(""):
            if hasattr(self, baseCut):
                baseCut = getattr(self, baseCut)
            else:
                raise Exception("baseCut for %s (%s) is not recognized in the class... it must be defined first"%(name, baseCut) )
        cutInst = CutClass( name, cutList, baseCut)
        if update:
            setattr(self, name, cutInst)
            self.cutInstList.append(name)
            self.cutInsts[name] = cutInst
        return cutInst

    def _getRegionCutNames(self, regionName):
        if not regionName in self.regions:
            raise Exception("Region (%s) not found among regions: %s"%(regionName, self.regions.keys()))
        region  = self.regions[regionName]
        region_cut_names = region['cuts'] if 'cuts' in region.keys() else []
        baseCut_cut_names = self._getRegionCutNames( region['baseCut'] ) if region['baseCut'] else []
        ret = baseCut_cut_names
        ret.extend([c for c in region_cut_names if c not in baseCut_cut_names])
        return ret 
        

    def _findVarsInCutListNames(self, varList, cutListNames):
        cutList = self._getCut( cutListNames, cutList=True)
        #cuts    = [c[1] for c  in cutList]
        #   if hasattr(self.vars, var):
        #       var = getattr(self.vars, var)
        if type(varList)==str:
            varList = [varList]
        matchedCutNames = []
        for var in varList:
            for cut_name, cut_string in cutList:
                if var in cut_string:
                    matchedCutNames.append(cut_name)
        return matchedCutNames

    def _makeNMinus1CutList(self, nMinus1Vars, cutListNames, makeCutInst = True, verbose = False):
        cutListNamesFull = self._getCut( cutListNames, namesOnly=True, returnString = False)
        matchedCutNames = self._findVarsInCutListNames( nMinus1Vars , cutListNamesFull )
        for v in nMinus1Vars:
            if v in cutListNamesFull:
                matchedCutNames.append(v)
        cutListNames_   = self._getCut( cutListNames, namesOnly=True, returnString = False) 
        newCutListNames = [ cut_name for cut_name in cutListNames_ if cut_name not in matchedCutNames]
        cutList = self._getCut( newCutListNames , cutList = True)

        nMinus1Name = '_'.join(cutListNames)+("_no"+"_no".join(matchedCutNames) if matchedCutNames else "")
        if makeCutInst:
            cutInst = self._makeCutClass( nMinus1Name, cutList= cutList, update=False)
        else:
            cutInst = None
        if verbose:
            print "nMinus1Name", nMinus1Name
            print "matchedCutNames", matchedCutNames

        return matchedCutNames , newCutListNames , cutInst


    def _getCut( self, cutListNames, returnString = True, namesOnly=False, cutList = False): 
        """
            get cut string either from cuts or from the regions
        """
        cuts_to_combine = []
        cut_names       = []
        for cutName in cutListNames:
            if cutName in self.cuts_dict.keys():
                cut_names.append( cutName )
                #cuts_to_combine.append( self.cuts_dict[cutName]['cut'] )
            if cutName in self.regions:
                region_cut_names = self._getRegionCutNames( cutName)
                region_cuts = self._getCut( region_cut_names, returnString = False )
                cut_names.extend(region_cut_names)
                #cuts_to_combine.extend( region_cuts)
        #print cutListNames
        #print cut_names
        unique_cut_names = []  ## in case of redundant cuts
        for cut in cut_names:
            if cut not in unique_cut_names:
                unique_cut_names.append(cut)
        if namesOnly:
            return unique_cut_names
        cuts_to_combine = [ self.cuts_dict[cutName]['cut'] for cutName in unique_cut_names ]
        if cutList:
            return map(list, zip(unique_cut_names, cuts_to_combine) )
        if returnString:
            ret = '&&'.join(["(%s)"%c for c in cuts_to_combine])    
        else:
            ret = cuts_to_combine
        return ret
    
    def addCut(self, region, cutName): 
        """
        add cut to region
        """
        cutListNames = [] 
        
        if region in self.regions:
            region_cut_names = self._getRegionCutNames(region)

            if cutName in region_cut_names:
               print "Cut %s found in region %s. No changes made."%(cutName, region)
               return region
            
            baseRegion = self.regions[region]
            newRegion = copy.deepcopy(baseRegion)
            newRegion['cuts'].append(cutName)
            
            newRegionName = '%s_plus_%s'%(region, cutName)
            
            self.regions[newRegionName] = newRegion

            self._update(reset = False)   
         
            print "Adding cut %s to %s to create %s region."%(cutName, region, newRegionName)
            return newRegionName 
 
    def removeCut(self, region, cutName): 
        """
        remove cut from region
        """
        cutListNames = [] 
        
        if region in self.regions:
            region_cut_names = self._getRegionCutNames(region)
            if cutName in region_cut_names:
               region_cut_names.remove(cutName)
            else:
               print "Cut %s not found in region %s. No changes made."%(cutName, region)
               return region
            
            baseRegion = self.regions[region]
           
            newRegion = {'baseCut':None, 'latex':''}
            newRegion['cuts'] = region_cut_names
         
            newRegionName = '%s_no_%s'%(region, cutName)
   
            self.regions[newRegionName] = newRegion
            self._update(reset = False)
       
            print "Removing cut %s from %s to create %s region."%(cutName, region, newRegionName)
            return newRegionName 

    def _getCutWeight(self, cutListNames, weightListNames, options = None ):
        cutString    = self._getCut( cutListNames)
        weightString = self.weights.combine( weightListNames) 
        return cutString, weightString

    def _getCutWeightString(self, cutListNames, weightNames, options = None):
        cutString , weightString = self._getCutWeight(cutListNames, weightNames)
        return "(%s)*(%s)"%(cutString, weightString)

    def _evaluateWeightOptions(self, sample, cutListNames, weightListNames, options):
        cutListNames = cutListNames[:]
        weightListNames = weightListNames[:]

        for option in options:
            #print option
            if not option in self.weights.cut_weight_funcs:
                print "option not found"
                assert False, option
                #continue
            opt_func = self.weights.cut_weight_funcs[option]
            #print opt_func
            #print sample, cutListNames, weightListNames
            sample, cutListNames, weightListNames = opt_func(sample, cutListNames, weightListNames)
            #print sample, cutListNames, weightListNames
        return sample, cutListNames, weightListNames


    def getSampleTriggersFilters(self, sample, cutString='', weightString=''):
        """ NOT FULLY IMPLEMENTED YET """
        if not hasattr(sample, "addFriendTrees"):
            raise Exception("Function only compatible with instances of Sample class")
        triggers = getattr(sample, 'triggers','')
        filters = getattr(sample, 'filters','')
        cuts = getattr(sample, 'cut','')
        weight = getattr(sample, 'weight','')

        cutList = []
        for cutItem in [cutString, triggers, filters, cuts] :
            if cutItem:
                cutList.append(cutItem)
        #print '----',cutList
        #print [cutString, triggers, filters, cuts]
        #print '--------------'

        weightList = [weightString] if weightString else []
        #print "....... before ", weightList
        if weight and weight.replace("(","").replace(")","") != "weight":
            weightList.append(weight) 
        ret_weights = "*".join(["(%s)"%w for w in weightList])
        cutList = []
        for cutItem in [cutString, triggers, filters, cuts] :
            if cutItem:
                cutList.append(cutItem)
        ret_cuts = "&&".join(["(%s)"%c for c in cutList])
        return ret_cuts, ret_weights


    def getSampleFullCutWeights(self, sample, cutListNames, weightListNames=[], options=None , nMinus1=None):
        if not hasattr(sample, "addFriendTrees"):
            raise Exception("Function only compatible with instances of Sample class")


        if nMinus1: #and nMinus1 in cutListNames:
            print "*****" 
            print "nMinus1:", nMinus1, cutListNames, weightListNames
            matched_cuts, cutListNamesMinus, nminus1_cuts = self._makeNMinus1CutList( nMinus1, cutListNames )
            matched_weights, weightListNamesMinus, nminus1_weight = self._makeNMinus1CutList( nMinus1, weightListNames , makeCutInst=False)
            print "matched cuts:", matched_cuts
            #cutListNamesMinus =[ c for c in cutListNames if c not in matched_cuts]
            print "nminus1_cuts:", cutListNamesMinus
            #print nminus1_cutlist
            samplename , cutListNames_, weightListNames_ = self.getSampleCutWeight( sample, cutListNamesMinus , weightListNamesMinus , options, returnString = False , returnCutWeight = False)
            c,w  = self._getCutWeight( cutListNames_ , weightListNames_ )
            #print c, w
        else:
            samplename , cutListNames_, weightListNames_ = self.getSampleCutWeight( sample, cutListNames, weightListNames , options, returnString = False , returnCutWeight = False)
            c,w = self._getCutWeight( cutListNames_, weightListNames_)

        c,w = self.getSampleTriggersFilters( sample, c, w)
        return c,w 

    def getSampleCutWeight(self, sample, cutListNames, weightListNames=None,  options=None, returnString = False, returnCutWeight=True):
        if not weightListNames:
            weightListNames = self.def_weights
        if not options:
            options = self.options
        cutListNames = self._getCut(cutListNames, namesOnly=True)
        sample, cutListNames, weightListNames  = self._evaluateWeightOptions(sample, cutListNames, weightListNames, options)
        if returnString:
            return "(%s)*(%s)"%self._getCutWeight(cutListNames, weightListNames)
        if returnCutWeight:
            return self._getCutWeight(cutListNames, weightListNames)
        return sample, cutListNames, weightListNames


class CutsWeights():
   def __init__(self, samples, cutWeightOptions = cutWeightOptions, nMinus1 = None, alternative_vars = {}):
      self.samples = samples
      self.cutWeightOptions = cutWeightOptions
      self.alternative_vars = alternative_vars
      self.cuts = Cuts(self.cutWeightOptions['settings'], self.cutWeightOptions['def_weights'], self.cutWeightOptions['options'], alternative_vars)
      self._update()

   def _update(self):
      self.cuts_weights = self.getCutsWeights(self.samples, self.cuts)

   def getCutsWeights(self, samples, cuts, nMinus1 = None):
      cuts_weights = {}

      regions = [x for x in cuts.regions if not 'bins' in x]

      for reg in regions:
         cuts_weights[reg] = {}

         for samp in samples:
            c,w = cuts.getSampleFullCutWeights(samples[samp], cutListNames = [reg], nMinus1 = nMinus1)

            cuts_weights[reg][samp] = (c,w)

      return cuts_weights

if __name__ == '__main__':

    settings = cutWeightOptions['settings']

    cuts = Cuts(settings)
