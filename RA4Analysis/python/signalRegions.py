# loop looks like this: for njb in signalRegion2fb: for stb in signalRegion2fb[njb]: for htb in signalRegion2fb[njb][stb]: print signalRegion2fb[njb][stb][htb]['deltaPhi']

signalRegion40pb = {(5,5): {(250, 350): {(500, -1): {'deltaPhi': .5}},
                            (350, -1):  {(500, -1): {'deltaPhi': .5}}},
                    (6,-1):{(250, 350): {(500, -1): {'deltaPhi': .5}},
                            (350, -1):  {(500, -1): {'deltaPhi': .5}}}
                   }

signalRegionCRonly = {(5,5): {(250, -1): {(500, -1): {'deltaPhi': .5}}},
                    (6,-1):{(250, -1): {(500, -1): {'deltaPhi': .5}}}
                   }
oneRegion = {(5,5): {(250, 350): {(500, -1): {'deltaPhi': 1.}}}}

smallRegion = {(5,5): {(250, 350): {(500, -1): {'deltaPhi': 1.}}},
               (6,7):{(250, 350): {(500, 750): {'deltaPhi': 1.}}}
              }

signalRegion2fb = {(5, 5): {(250, 350): {(500, -1): {'deltaPhi': 1.0}},
                            (350, 450): {(500, -1): {'deltaPhi': 1.0}},
                            (450, -1): {(500, -1): {'deltaPhi': 1.0}}},
                   (6, 7): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                         (750, -1): {'deltaPhi': 1.0}},
                            (350, 450): {(500, -1): {'deltaPhi': 1.0}},
                            (450, -1): {(500, 750): {'deltaPhi': 1.0},
                                        (750, -1): {'deltaPhi': 1.0}}},
                   (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                          (750, -1): {'deltaPhi': 1.0}},
                             (350, 450): {(500, -1): {'deltaPhi': 1.0}},
                             (450, -1): {(500, 750): {'deltaPhi': 1.0},
                                         (750, -1): {'deltaPhi': 1.0}}}
                  }

signalRegion3fbStaticDPhi = {(5, 5): {(250, 350): {(500, -1):   {'deltaPhi': 1.0}},
                            (350, 450): {(500, -1):   {'deltaPhi': 1.0}},
                            (450, -1): {(500, -1):    {'deltaPhi': 1.0}}},
                   (6, 7): {(250, 350): {(500, 750):  {'deltaPhi': 1.0},
                                         (750, -1):   {'deltaPhi': 1.0}},
                            (350, 450): {(500, 750):  {'deltaPhi': 1.0},
                                         (750, -1):   {'deltaPhi': 1.0}},
                            (450, -1): {(500, 750):   {'deltaPhi': 1.0},
                                        (750, 1250):  {'deltaPhi': 1.0},
                                        (1250, -1):   {'deltaPhi': 1.0}}},
                   (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                          (750, -1):  {'deltaPhi': 1.0}},
                             (350, 450): {(500, -1):  {'deltaPhi': 1.0}},
                             (450, -1): {(500, -1):   {'deltaPhi': 1.0}}}}


#signalRegion3fb = {(5, 5): {(250, 350): {(500, -1):   {'deltaPhi': 1.0}},
#                            (350, 450): {(500, -1):   {'deltaPhi': 1.0}},
#                            (450, -1): {(500, -1):    {'deltaPhi': 1.0}}},
#                   (6, 7): {(250, 350): {(500, 750):  {'deltaPhi': 1.0},
#                                         (750, -1):   {'deltaPhi': 1.0}},
#                            (350, 450): {(500, 750):  {'deltaPhi': 1.0},
#                                         (750, -1):   {'deltaPhi': 1.0}},
#                            (450, -1): {(500, 750):   {'deltaPhi': 0.75},
#                                        (750, 1250):  {'deltaPhi': 0.75},
#                                        (1250, -1):   {'deltaPhi': 0.75}}},
#                   (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
#                                          (750, -1):  {'deltaPhi': 1.0}},
#                             (350, 450): {(500, -1):  {'deltaPhi': 0.75}},
#                             (450, -1): {(500, -1):   {'deltaPhi': 0.75}}}}

signalRegion3fb = {(5, 5):  {(250, 350): {(500, -1):   {'deltaPhi': 1.0, 'njet':'5j','LT':'LT1','HT': 'HTi',      'tex':'\\textrm{LT1}, \\textrm{HTi}'}},
                             (350, 450): {(500, -1):   {'deltaPhi': 1.0, 'njet':'5j','LT':'LT2','HT': 'HTi',      'tex':'\\textrm{LT2}, \\textrm{HTi}'}},
                             (450, -1):  {(500, -1):   {'deltaPhi': 1.0, 'njet':'5j','LT':'LT3','HT': 'HTi',      'tex':'\\textrm{LT3}, \\textrm{HTi}'}}},
                   (6, 7):  {(250, 350): {(500, 750):  {'deltaPhi': 1.0, 'njet':'6-7j','LT':'LT1','HT': 'HT1',    'tex':'\\textrm{LT1}, \\textrm{HT1}'},
                                          (750, -1):   {'deltaPhi': 1.0, 'njet':'6-7j','LT':'LT1','HT': 'HT23',   'tex':'\\textrm{LT1}, \\textrm{HT23}'}},
                             (350, 450): {(500, 750):  {'deltaPhi': 1.0, 'njet':'6-7j','LT':'LT2','HT': 'HT1',    'tex':'\\textrm{LT2}, \\textrm{HT1}'},
                                          (750, -1):   {'deltaPhi': 1.0, 'njet':'6-7j','LT':'LT2','HT': 'HT23',   'tex':'\\textrm{LT2}, \\textrm{HT23}'}},
                             (450, -1):  {(500, 1000): {'deltaPhi': 0.75, 'njet':'6-7j','LT':'LT3','HT': 'HT12',  'tex':'\\textrm{LT3}, \\textrm{HT12}'},
                                          (1000, -1):  {'deltaPhi': 0.75, 'njet':'6-7j','LT':'LT3','HT': 'HT3',   'tex':'\\textrm{LT3}, \\textrm{HT3}'}}},
                   (8, -1): {(250, 350): {(500, 750):  {'deltaPhi': 1.0, 'njet':'#geq8j','LT':'LT1','HT': 'HT1',  'tex':'\\textrm{LT1}, \\textrm{HT1}'},
                                          (750, -1):   {'deltaPhi': 1.0, 'njet':'#geq8j','LT':'LT1','HT': 'HT23', 'tex':'\\textrm{LT1}, \\textrm{HT23}'}},
                             (350, 450): {(500, -1):   {'deltaPhi': 0.75, 'njet':'#geq8j','LT':'LT2','HT': 'HTi', 'tex':'\\textrm{LT2}, \\textrm{HTi}'}},
                             (450, -1):  {(500, -1):   {'deltaPhi': 0.75, 'njet':'#geq8j','LT':'LT3','HT': 'HTi', 'tex':'\\textrm{LT3}, \\textrm{HTi}'}}}}

signalRegion3fbMerge = {(5, 5):  {(450, -1):  {(500, -1):   {'deltaPhi': 0.75, 'njet':'5j','LT':'L_{T}3','HT': 'H_{T}i'}}},
                        (6, 7):  {(450, -1):  {(500, 750):  {'deltaPhi': 0.75, 'njet':'6-7j','LT':'L_{T}3','HT': 'H_{T}12'},
                                               (750, -1):   {'deltaPhi': 0.75, 'njet':'6-7j','LT':'L_{T}3','HT': 'H_{T}3'}}},
                        (8, -1): {(350, 450): {(500, -1):   {'deltaPhi': 1.0,  'njet':'#geq8j','LT':'L_{T}2','HT': 'H_{T}i'}}}}

signalRegion3fbReduced = {(5, 5):  {(250, 350): {(500, -1):  {'deltaPhi': 1.0, 'name':'5j, L_{Tl}, H_{Ti}'}},
                                    (350, 450): {(500, -1):  {'deltaPhi': 1.0, 'name':'5j, L_{Tm}, H_{Ti}'}},
                                    (450, -1):  {(500, -1):  {'deltaPhi': 0.75, 'name':'5j, L_{Th}, H_{Ti}'}}},
                          (6, 7):  {(250, 350): {(500, 750): {'deltaPhi': 1.0, 'name':'6-7j, L_{Tl}, H_{Tl}'},
                                                 (750, -1):  {'deltaPhi': 1.0, 'name':'6-7j, L_{Tl}, H_{Tmh}'}},
                                    (350, 450): {(500, 750): {'deltaPhi': 1.0, 'name':'6-7j, L_{Tm}, H_{Tl}'},
                                                 (750, -1):  {'deltaPhi': 1.0, 'name':'6-7j, L_{Tm}, H_{Tmh}'}},
                                    (450, -1):  {(500, 750): {'deltaPhi': 0.75, 'name':'6-7j, L_{Th}, H_{Tl}'},
                                                 (750, -1):  {'deltaPhi': 0.75, 'name':'6-7j, L_{Th}, H_{Tmh}'}}},
                          (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0, 'name':'#geq8j, L_{Tl}, H_{Tl}'},
                                                 (750, -1):  {'deltaPhi': 1.0, 'name':'#geq8j, L_{Tl}, H_{Tmh}'}},
                                    (350, -1):  {(500, -1):  {'deltaPhi': 0.75, 'name':'#geq8j, L_{Tmh}, H_{Ti}'}}}}

validationRegion = {(4, 4):  {(250, 350): {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}1','HT': 'H_{T}i'}},
                             (350, 450): {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}2','HT': 'H_{T}i'}},
                             (450, -1):  {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}3','HT': 'H_{T}i'}}}}

validationRegion2 = {(4, 4):  {(250, -1): {(500, 750):   {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}i','HT': 'H_{T}1'},
                                           (750, 1000):  {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}i','HT': 'H_{T}2'},
                                           (1000, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'L_{T}i','HT': 'H_{T}3'}}}}

validationRegionAll = {(4, 4):  {(250, 350): {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'LT1','HT': 'HTi'},
                                              (500, 750):  {'deltaPhi': 1.0, 'njet':'4j','LT':'LT1','HT': 'HT1'},
                                              (750, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'LT1','HT': 'HT23'}},
                                 (350, 450): {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'LT2','HT': 'HTi'},
                                              (500, 750):  {'deltaPhi': 1.0, 'njet':'4j','LT':'LT2','HT': 'HT1'},
                                              (750, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'LT2','HT': 'HT23'}},
                                 (450, -1):  {(500, -1):   {'deltaPhi': 1.0, 'njet':'4j','LT':'LT3','HT': 'HTi'},
                                              (500, 1000): {'deltaPhi': 0.75, 'njet':'4j','LT':'LT3','HT': 'HT12'},
                                              (1000, -1):  {'deltaPhi': 0.75, 'njet':'4j','LT':'LT3','HT': 'HT3'}}}}

newBins3fb = {(5, 5):  {(450, -1): {(500, -1):    {'deltaPhi': 0.75}}},
              (6, 7):  {(450, -1): {(500, 750):   {'deltaPhi': 0.75},
                                    (750, -1):    {'deltaPhi': 0.75}}},
              (8, -1): {(350, -1): {(500, -1):    {'deltaPhi': 0.75}}}}


sideBand3fb =     {(4, 5): {(250, 350): {(500, -1):   {'deltaPhi': 1.0},
                                         (500, 750):  {'deltaPhi': 1.0},
                                         (750, -1):   {'deltaPhi': 1.0}},
                            (350, 450): {(500, -1):   {'deltaPhi': 1.0},
                                         (500, 750):  {'deltaPhi': 1.0},
                                         (750, -1):   {'deltaPhi': 1.0}},
                            (450, -1): {(500, 1000):   {'deltaPhi': 0.75},
                                        (1000, -1):   {'deltaPhi': 0.75},
                                        (500, -1):   {'deltaPhi': 0.75}}}}

#sideBand3fb =     {(4, 5): {(250, 350): {(500, -1):   {'deltaPhi': 1.0},
#                                         (500, 750):  {'deltaPhi': 1.0},
#                                         (750, -1):   {'deltaPhi': 1.0}},
#                            (350, 450): {(500, -1):   {'deltaPhi': 1.0},
#                                         (500, 750):  {'deltaPhi': 1.0},
#                                         (750, -1):   {'deltaPhi': 1.0}},
#                            (450, -1): {(500, 750):   {'deltaPhi': 0.75},
#                                        (750, 1250):  {'deltaPhi': 0.75},
#                                        (1250, -1):   {'deltaPhi': 0.75},
#                                        (500, -1):   {'deltaPhi': 0.75}}}}

#signalRegion3fb = {(5, 5): {(250, 350): {(500, -1): {'deltaPhi': 1.0}},
#                            (350, 450): {(500, -1): {'deltaPhi': 1.0}},
#                            (450, -1): {(500, -1): {'deltaPhi': 1.0}}},
#                   (6, 7): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
#                                         (750, -1): {'deltaPhi': 1.0}},
#                            (350, 450): {(500, 750): {'deltaPhi': 1.0},
#                                         (750, -1): {'deltaPhi': 1.0}},
#                            (450, -1): {(500, 750): {'deltaPhi': 0.75},
#                                        (750, 1250): {'deltaPhi': 0.75},
#                                        (1250, -1): {'deltaPhi': 0.75}}},
#                   (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
#                                          (750, -1): {'deltaPhi': 1.0}},
#                             (350, 450): {(500, 750): {'deltaPhi': 0.75},
#                                          (750, -1): {'deltaPhi': 0.75}},
#                             (450, -1): {(500, 1000): {'deltaPhi': 0.75},
#                                         (1000, -1): {'deltaPhi': 0.75}}}}

signalRegion10fb =  {(5, 5): {(250, 350): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (350, 450): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (450, -1): {(500, 750):     {'deltaPhi': 1.0},
                                          (750, 1000):    {'deltaPhi': 1.0},
                                          (1000, -1):     {'deltaPhi': 1.0}}},

                     (6, 7): {(250, 350): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (350, 450): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (450, -1): {(500, 750):     {'deltaPhi': 0.75},
                                          (750, 1000):    {'deltaPhi': 0.75},
                                          (1000, -1):     {'deltaPhi': 0.75}}},

                     (8, -1): {(250, 350): {(500, 750):   {'deltaPhi': 1.0},
                                            (750, 1000):  {'deltaPhi': 1.0},
                                            (1000, -1):   {'deltaPhi': 1.0}},
                               (350, 450): {(500, 750):   {'deltaPhi': 0.75},
                                            (750, 1000):  {'deltaPhi': 0.75},
                                            (1000, -1):   {'deltaPhi': 0.75}},
                               (450, -1): {(500, 750):    {'deltaPhi': 0.75},
                                           (750, 1000):   {'deltaPhi': 0.75},
                                           (1000, -1):    {'deltaPhi': 0.75}}}
                    }

sideBand10fb =  {(4, 5):     {(250, 350): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (350, 450): {(500, 750):    {'deltaPhi': 1.0},
                                           (750, 1000):   {'deltaPhi': 1.0},
                                           (1000, -1):    {'deltaPhi': 1.0}},
                              (450, -1): {(500, 750):     {'deltaPhi': 1.0},
                                          (750, 1000):    {'deltaPhi': 1.0},
                                          (1000, -1):     {'deltaPhi': 1.0}}}}

signalRegion10fbStaticDPhi =  {(5, 5): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                           (750, 1000): {'deltaPhi': 1.0},
                                           (1000, 1250): {'deltaPhi': 1.0},
                                           (1250, -1): {'deltaPhi': 1.0}},
                              (350, 450): {(500, 750): {'deltaPhi': 1.0},
                                           (750, 1000): {'deltaPhi': 1.0},
                                           (1000, 1250): {'deltaPhi': 1.0},
                                           (1250, -1): {'deltaPhi': 1.0}},
                              (450, -1): {(500, 750): {'deltaPhi': 1.0},
                                          (750, 1000): {'deltaPhi': 1.0},
                                          (1000, 1250): {'deltaPhi': 1.0},
                                          (1250, -1): {'deltaPhi': 1.0}}},
                     (6, 7): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                           (750, 1000): {'deltaPhi': 1.0},
                                           (1000, 1250): {'deltaPhi': 1.0},
                                           (1250, -1): {'deltaPhi': 1.0}},
                              (350, 450): {(500, 750): {'deltaPhi': 1.0},
                                           (750, 1000): {'deltaPhi': 1.0},
                                           (1000, 1250): {'deltaPhi': 1.0},
                                           (1250, -1): {'deltaPhi': 1.0}},
                              (450, -1): {(500, 750): {'deltaPhi': 1.0},
                                          (750, 1000): {'deltaPhi': 1.0},
                                          (1000, 1250): {'deltaPhi': 1.0},
                                          (1250, -1): {'deltaPhi': 1.0}}},
                     (8, -1): {(250, 350): {(500, 750): {'deltaPhi': 1.0},
                                            (750, 1000): {'deltaPhi': 1.0},
                                            (1000, 1250): {'deltaPhi': 1.0},
                                            (1250, -1): {'deltaPhi': 1.0}},
                               (350, 450): {(500, 750): {'deltaPhi': 1.0},
                                            (750, 1000): {'deltaPhi': 1.0},
                                            (1000, 1250): {'deltaPhi': 1.0},
                                            (1250, -1): {'deltaPhi': 1.0}},
                               (450, -1): {(500, 750): {'deltaPhi': 1.0},
                                           (750, 1000): {'deltaPhi': 1.0},
                                           (1000, 1250): {'deltaPhi': 1.0},
                                           (1250, -1): {'deltaPhi': 1.0}}}
                    }
