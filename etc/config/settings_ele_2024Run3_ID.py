
#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passingMVAhzzWinter22'  : '(passingMVAhzzWinter22 == 1 && fabs(el_sip) < 4 && fabs(el_dz) < 1 && fabs(el_dxy) < 0.5)', #Martina new ID hzzWinter22 with 22 training
    #'passingReco' : '(passingRECO ==1)',
    #'passingRecoED' : '(passingRECOEcalDriven ==1 && passingRECOTrackDriven==0)',
    #'passingRecoTD' : '(passingRECOTrackDriven ==1 && passingRECOEcalDriven==0)',
    #
    #'passingCutBasedVeto94XV2'    : '(passingCutBasedVeto94XV2   == 1)',
    #'passingCutBasedLoose94XV2'   : '(passingCutBasedLoose94XV2  == 1)',
    #'passingCutBasedMedium94XV2'  : '(passingCutBasedMedium94XV2 == 1)',
    #'passingCutBasedTight94XV2'   : '(passingCutBasedTight94XV2  == 1)',
    #'passingMVA94Xwp80isoV2' : '(passingMVA94Xwp80isoV2 == 1)',
    #'passingMVA94Xwp90isoV2' : '(passingMVA94Xwp90isoV2 == 1)',
    #'passingMVA94Xwp80noisoV2' : '(passingMVA94Xwp80noisoV2 == 1)',
    #'passingMVA94Xwp90noisoV2' : '(passingMVA94Xwp90noisoV2 == 1)',
    #'passingMVA94XwpLisoV2'    : '(passingMVA94XwpLisoV2 == 1)',
    #'passingMVA94XwpLnoisoV2'  : '(passingMVA94XwpLnoisoV2 == 1)',
    #'passingMVA94XwpHZZisoV2'  : '(passingMVA94XwpHZZisoV2 == 1)',
    
    }

#
baseOutDir = '/eos/user/m/mmanoni/Tnp_results_2024/hzzWinter22/2024Results/'
#baseOutDir = 'results/Run3_2024ID/tnpEleIDs'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'
#tnpTreeDir = 'tnpEleReco'

samplesDef = {
    #'data'   : tnpSamples.Run3_2024['data_Run2024I'].clone(),
    'data'    : tnpSamples.Run3_2024ID['data_Run2024'].clone(),
    
    #'mcNom'  : tnpSamples.Run3_2024['DY_amcatnlo'].clone(),
    'mcNom'  : tnpSamples.Run3_2024ID['DYto2E'].clone(),
    
    #'mcAlt'  : tnpSamples.Run3_2024['DY_amcatnlo'].clone(),
    'mcAlt'    : tnpSamples.Run3_2024ID['DYto2E'].clone(),
    #'tagSel' : tnpSamples.Run3['DY_madgraph'].clone(),
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Run3_2024['data_Run2024B'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_2024['data_Run2024F'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_2024['data_Run2024H'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_2024['data_Run2024I'] )
#
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3D'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3E'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3F'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3G'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')

#samplesDef['data'  ].set_cut('run >= 379412 && run <= 380252 ') # 2024 C
#samplesDef['data' ].set_cut('run <= 380252') # 2024 C
samplesDef['data' ].set_tnpTree(tnpTreeDir)


if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)

##if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
##if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
##if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
##if not samplesDef['tagSel'] is None:
##    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
##    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut


## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_data_Run2022_B-G.totWeight'
#weightName = 'weights_data_Run2022_inclusive.totWeight'
weightName = 'weights_2024_run2024.totWeight'

#puFile = '/eos/cms/store/group/phys_egamma/tnpTuples/bjoshi/2023-04-25/2022/pu/DY_1j_madgraph_PromptReco2022FG_tnpPhoID.pu.puTree.root'
puFile ='/eos/cms/store/group/phys_egamma/ochando/tnpTuples/PU_Trees/DY_amcatnlo_ele.pu.puTree.root'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree(puFile)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree(puFile)

##if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
##if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
##if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_miniAOD/DY_amcatnloext_ele.pu.puTree.root')
##if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] }, # for ID HZZ
    #{ 'var' : 'el_pt' , 'type': 'float', 'bins': [10,20,35,50,100,500] },
    #{ 'var' : 'abs(sc_eta)' , 'type': 'float', 'bins': [0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] },  #-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
    #
    #{ 'var' : 'sc_abseta' , 'type': 'float', 'bins': [0.0, 0.5, 1.0, 1.444, 1.566, 2.0, 2.5] }, #medium high pT
    #{ 'var' : 'sc_abseta' , 'type': 'float', 'bins': [0.0, 1.0, 1.444, 1.566, 2.0, 2.5] }, #low pT
    #
    #{ 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -1.0, -0.5, 0.0, 0.5, 1.0, 1.4442, 1.566, 2.0, 2.5] },
    #{ 'var' : 'sc_pt' , 'type': 'float', 'bins': [10,20,45,75,100,500] },
    #
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 15, 20, 35, 50, 100, 500] }, # ID HZZ
    #{ 'var' : 'sc_pt' , 'type': 'float', 'bins': [10,20] }, # low pT
    #{ 'var' : 'sc_pt' , 'type': 'float', 'bins': [20,45, 75] }, #medium pT
    #{ 'var' : 'sc_pt' , 'type': 'float', 'bins': [75,100,500] }, #high pT
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'
cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && el_q*tag_Ele_q < 0'
#&& sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60' 

#&& mcTrue==1'
#cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 && (sc_tkIso/sc_pt)<0.15'
#cutBase = 'tag_Ele_pt > 45 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 && (sc_tkIso/sc_pt)<0.15' #lowpT
#cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 && (sc_tkIso/sc_pt)<0.20'
#cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 && (sc_tkIso/sc_pt)<0.15'

additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    1 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    2 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    3 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    4 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    5 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    6 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    7 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    8 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    9 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.5,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    # --CMSShape
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]", #midpT #bin 22/27
    #"acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2.]","peakP[90.0]", #lowpT MARTINA 
    #
    #"acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]", #midpT #bin 22/27

    #"acmsF[90.,50.,130.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]", # ID default
    #"acmsF[69.,50.,100.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]", #ID bin 11
    #"acmsF[90.,50.,130.]","betaF[0.05,0.01,0.09]","gammaF[0.1, -2, 2]","peakF[90.0]", #ID bin 13 14
    #"acmsF[40.,30.,130.]","betaF[0.01,0.01,0.15]","gammaF[0.5, -2, 2]","peakF[90.0]", #ID bin 16
    #"acmsF[40.,30.,500.]","betaF[0.08,0.01,0.15]","gammaF[0.1, -2, 2]","peakF[90.0]", #ID bin 18
    #"acmsF[50.,30.,500.]","betaF[0.09,0.01,0.15]","gammaF[0.2, -2, 2]","peakF[90.0]", #ID bin 23 25 26 #HERE
    ##acmsF[90.,50.,130.]","betaF[0.028,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]", #midpT bin08
    #"acmsF[0.5,0.,100.]","betaF[0.02,0.01,1.3]","gammaF[0.1, -2, 2]","peakF[90.0]", #lowpT bin00

    #--Chebyschev
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}",#bin 0/1/2/3/4/6
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.2,0.2],a3[0, -0.5, 0.5]}",#bin 5 
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-1.0,1.0],a3[0, -0.5, 0.5]}" #bin 7/13/14/15/16
    "{a0[-0.9,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-1.0,1.0],a3[0, -0.5, 0.5]}",#bin  20-29

    #"a0[12., 1., 15.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]",
    
    #-- Bernstein
    #"a0[12., 5., 15.]", "a1[2, 0., 3.]", "a2[2., -0., 5.]", "a3[0.3, -0., 3.]", #Nominal lowpT bins (0-9) MARTINA
    
    ]

tnpParAltSigFit = [
    #SIGN
    #sigmaP[15.0,15.0,20.0
    "meanP[-0.0,-5.0,5.0]","sigmaP[1.,0.,15.0]","alphaP[2.0,1.0,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]", #DY ID MARTINA #bin 18 /ALL DATA BINS
   
    #"meanP[-3.,-5.0,5.0]","sigmaP[30.0, 1.,40.0]","alphaP[20.0, 15.0, 25.0]" ,'nP[5,4,6]',"sigmaP_2[20.0, 15.0, 25.0]","sosP[3.0, 2.0, 4.0]", #DY ID MARTINA #bin 22

    #"meanF[-0.0,-5.0,5.0]","sigmaF[10.0]","alphaF[1.0,0.8,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.0,10.0]","sosF[1,0.,8.0]",#DY ID MARTINA bin 12/17 sigmaF[10.0] fixed--> impossible to fit oth
    #
    "meanF[-0.0,-5.0,5.0]","sigmaF[1.,0.,15.0]","alphaF[2.5,1.0,3.0]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.,8.0]",#DY ID MARTINA
    #"meanF[-0.0,-5.0,5.0]","sigmaF[10.,9.,11.]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.,8.0]",#DY bin 01/02/03/18 MARTINA

    #bin 27
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,10.0]","alphaP[2.0,0.5,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]", #DY ID MARTINA #bin 27
    #"meanF[-0.0,-5.0,5.0]","sigmaF[10.,0.,11.]","alphaF[2.0,0.5,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.,8.0]",#DY bin 27 MARTINA

    # --CMSShape BKG
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1.]","peakP[90.0]", #midpT MARTINA
 

    #"acmsF[50.,20.,500.]","betaF[0.026,0.01,0.16]","gammaF[1.5, -2., 2.]","peakF[90.0]", #ID bin 18 (all DY)
    #"acmsF[50.,20.,75.]","betaF[0.02,0.01,0.2]","gammaF[0.035, -2., 2.]","peakF[90.0]", #DATA bin 12/17/18/19
    #"acmsF[65.,50.,85.]","betaF[0.02,0.01,0.2]","gammaF[1.5, -2., 2.]","peakF[90.0]", #DATA bin 13
   

    #--Cheb
  # "{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.02,0.02],a3[0, -0.2, 0.2]}",#bin 0/1/3
   
   #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.1,0.1],a3[0, -0.2, 0.2]}",#bin 4
   #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.1,0.1],a3[0, -0.2, 0.2]}",#bin 5
   #"{a0[-1.0,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.04,0.04],a3[0, -0.2, 0.2]}",#bin 6/7
        #"{a0[-1.0,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-0.03,0.03],a3[0, -0.2, 0.2]}",#bin 8/9/15/16
        #"{a0[-0.5,-2.0, 0.5],a1[0.,-0.7,0.7],a2[0.,-0.02,0.02],a3[0, -0.1, 0.1]}",#bin 8/9/13/14
   #"{a0[-1.0,-1.5,-0.0],a1[0.,-0.5,0.5],a2[0.,-0.02,0.02],a3[0, -0.2, 0.2]}",#bin 6/7
   #"a0[12., 1., 15.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]",

    #"{a0[-0.9,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-0.9,0.9],a3[0, -0.5, 0.5]}",#bin 23-28

    "{a0[-0.9,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-1.0,1.0],a3[0, -0.1, 0.1]}",#bin  20/21/22/29

    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-3.0,3.0]","sigmaP[0.9,0.5,5.0]",
   # "meanP[-0.0,-2.0,1.0]","sigmaP[0.9,0.5,5.0]",#bin 27
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",

    # --- Exponential ALL
    "alphaP[0.,-5.,5.]", 
    #"alphaF[0.,-5.,5.]",

    # --- Bernstein LOW PT
    #"a0[12., 1., 15.]", "a1[2, 0., 3.]", "a2[0.5., -0., 0.8.]", "a3[0.3, -0., 3.]", #0-06/8
    #"a0[12., 1., 15.]", "a1[2, 0., 3.]", "a2[0.5., -0., 1.]", "a3[0.3, -0., 3.]", #bin 7
    #"a0[12., 1., 15.]", "a1[2., 0., 3.]", "a2[0.1, -0., 0.5]", "a3[0.3, -0., 3.]",  #bin 9/13/14/15/16 /20/21/22/23
    "a0[12., 0.9., 15.]", "a1[2., 0., 3.]", "a2[0.1, -0., 0.5]", "a3[0.3, -0., 3.]",  #bin 9/13/14/15/16 /20/21/22/23
    ]

tnpParAltSigBkgFit = [

    "meanP[-0.5,-5.0,5.0]","sigmaP[3,0.7,6.0]","alphaP[0.5,0.,5.5]" ,'nP[2,-5,5]',"sigmaP_2[0.1,0.,6.0]","sosP[0.02,0.,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",

    # --- Exponential
    "alphaP_2[0.,-5.,5.]",
    #"alphaF_2[0.,-5.,5.]",



    # --- Bernstein LOW PT

    #"a0[5., 1., 15.]", "a1[2., 0., 3.]", "a2[0.2, -0.5, 2.]", "a3[0.3, -0., 3.]",  #bin 0/3/4/5 8/9
    
    #"a0[12., 1., 15.]", "a1[2, 0., 2.]", "a2[0.3, -0.5, 1.5]", "a3[0.3, -0., 3.]", #bin 2
    #"a0[12., 1., 15.]", "a1[2, 0., 3.]", "a2[0.5., -0., 1.]", "a3[0.3, -0., 3.]", #bin 7
    
    
    #"a0[5., 1., 20.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]",  #bin 0/3/4/5 8/9 13/14/15/16 OK

    #"a0[5., 0.5, 20.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]",

    #"a0[1., 0., 1.]", "a1[2., -0., 10.]", "a2[2., -0., 10]", "a3[0, 0., 0.]",

    #"a0[1., -1., 3.]", "a1[1., -1., 2.]", "a2[0.2, -1, 2.]", "a3[0.3, -1., 0.5.]",

    #"a0[5., 4., 7.]", "a1[2., 0., 3.]", "a2[0.2, -0.7, 0.7]", "a3[0.3, -0.5, 0.5]",  #bin 0/3/4/5 8/9 13/14/15/16 OK
    #"a0[5., 1., 20.]", "a1[2., 0., 3.]", "a2[0.2, -0., 1.0]", "a3[0.3, -0., 3.]", #bin 16 OK



    #"a0[5., 1., 20.]", "a1[2., 0., 3.]", "a2[0.2, -0., 3.0]", "a3[0.3, -0., 3.]",  #bin 0/ 8/9

    #good--------

    #"a0[5., 1., 6.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]",  #bin 9

    #"a0[1.2., 1.1, 5.]", "a1[2., 0., 2.]", "a2[0.2, -0., 10]", "a3[0.3, -0., 3.]",


    #"a0[1.2., 1.1, 6.5]", "a1[2., 0., 3.]", "a2[2., 1.5, 5.]", "a3[0.3, -0., 3.]", #bin 3 OK

    #"a0[1.2., 1.1, 7.5]", "a1[2., 0., 3.]", "a2[2., 1.5, 5.]", "a3[0.3, -0., 3.]",#bin1 OK

    #"a0[4.9, 4.85, 4.95]", "a1[2.,1.95, 2.05]", "a2[2.15, 2.145, 2.151]", "a3[1.54, 1.50, 1.55]", #bin 9 OK

    "a0[4.80, 4.7, 4.9]", "a1[1.2, 1.15, 1.3]", "a2[2.7, 2.65, 2.8]", "a3[0.6, 0.55,0.7]", #bin 7

    #"a0[4.99]", "a1[1.]", "a2[2.]", "a3[0.1]", #bin 6

    #"a0[1.2., 1.1, 5.5]", "a1[2., 0., 2.]", "a2[4., 1., 10]", "a3[0.3, -0., 3.]", #bin 0 OK

    #"a0[1.2., 1.1, 5.5]", "a1[2., 0., 2.]", "a2[4., 1., 10]", "a3[0.3, -0., 3.]",

    #"a0[7., 6.5, 7.1]", "a1[2., 1.95, 3.0]", "a2[2.001, 2., 3.0]", "a3[0.001, 0., 0.01]", #bin 6 OK

    #"a0[1.2., 1.1, 5.5]", "a1[2., 0., 2.]", "a2[4., 1., 10]", "a3[0.3, -0., 3.]",





    #"a0P[0.5, -1., 1.]", "a1P[0., -2., 1.]", "a2P[0., -2., 1.]", #>75,
    #"a0P[1., -1., 1.]", "a1P[0.5, -2., 2.]", "a2P[0.5, -2., 2.]", #>75, # bin05, 06, 10
    #"a0P[2.5, -3.5, 3.5]", "a1P[-1., -3.5, 5.]", "a2P[0.5, -3.5, 5.5]", "a3P[2., -3.5, 3.5]", #10-20, bin0, 01
    #"a0P[2, -3.5, 3.5]", "a1P[2., -3.5, 5.]", "a2P[1.5, -3.5, 5.5]", "a3P[1.5, -3.5, 3.5]", #2024 ID
    #
    #"a0F[0.2, -2., 2.]", "a1F[0.2, -3., 2.]", "a2F[0., -1., 3.]", "a3F[0.5, -1., 3.]", #>75 bin03
    #"a0F[0.45, -2., 2.]", "a1F[0.85, -3., 2.]", "a2F[0.15, -1., 3.]", "a3F[2.5., -1., 4.]", #>75 bin04
    #"a0F[0.45, -2., 2.]", "a1F[0.84, -3., 2.]", "a2F[-0.05, -1., 3.]", "a3F[0.5, -0., 5.]", #>75 bin02
    #"a0F[0.45, -2., 2.]", "a1F[0.75, -3., 2.]", "a2F[0.5, -1., 3.]", "a3F[2.5., -0., 5.]", #>75 bin05, 06
    #"a0F[0.93, -2., 2.]", "a1F[0., -3., 2.]", "a2F[1.5, -1., 3.]", "a3F[2.9., -0., 5.]", #>75 bin 07
    #"a0F[0.7, -2., 2.]", "a1F[1.7, -3., 2.]", "a2F[0.5, -1., 3.]", "a3F[2.9., -0., 5.]", #>75 bin 08, 11
    #"a0F[1.7, -2., 2.]", "a1F[1.7, -3., 2.]", "a2F[0.5, -1., 3.]", "a3F[2.9., -0., 5.]", #>75 bin 09
    #"a0F[0., -2., 2.]", "a1F[0.16, -3., 2.]", "a2F[0.1, -0., 3.]", "a3F[1., -0., 5.]", #>75 bin 10
    #"a0F[0.25, -2., 2.]", "a1F[0.5, -3., 2.]", "a2F[0.5., -1., 3.]", "a3F[2.3, -1., 4.]", #>75
    #"a0F[0.5, -2., 2.]", "a1F[2., -1., 3.]", "a2F[0.6., -1., 3.]", "a3F[0.5, -1., 4.]", #midpT
    #"a0F[0.6, -0., 3.]", "a1F[2., -0., 5.]", "a2F[1.., -1., 3.]", "a3F[1.5, -0., 4.]", # midpT bin00 01 03
    #"a0F[0.2, -2., 2.]", "a1F[1.5, -0., 5.]", "a2F[0.1., -0., 5.]", "a3F[0.5, 0., 4.]", # midpT  07 08 09 10 11
    #"a0F[2.2, -0., 3.]", "a1F[2.5, -0., 5.]", "a2F[0.1., -0., 5.]", "a3F[0.1, 0., 4.]", # midpT  05
    #"a0F[0.03, -0., 3.]", "a1F[0.05, -0., 5.]", "a2F[0.025., -0., 5.]", "a3F[0.02, 0., 4.]", # midpT  04
    #"a0F[0.6, -0., 3.]", "a1F[2., -0., 5.]", "a2F[1.., -1., 3.]", "a3F[1.5, -0., 4.]", # 2024I midpT bin 02 08 09 10 11
    #"a0F[0.7, -0., 5.]", "a1F[2., -0., 5.]", "a2F[1.., -0., 3.]", "a3F[1.5, -0., 4.]", # 2024I midpT bin 00
    #"a0F[1.2, -0., 5.]", "a1F[3., -0., 5.]", "a2F[1.., -0., 3.]", "a3F[1.5, -0., 4.]", # 2024I midpT bin 01 04 05 06 #2024C bin00 06->11
    #"a0F[0.6, -0., 3.]", "a1F[2., -0., 5.]", "a2F[1.., -1., 3.]", "a3F[1.5, -0., 4.]", # 2024C midpT bin 01
    #"a0F[0.6, -0., 3.]", "a1F[1., -0., 5.]", "a2F[1.., -1., 4.]", "a3F[1.5, -0., 4.]", # 2024C midpT bin 02 04
    #"a0F[0.03, -0., 3.]", "a1F[0.06, -0., 6.]", "a2F[0.., -1., 5.]", "a3F[0.02, -0., 4.]", # 2024C midpT bin 05
    #"a0F[1.03, -0., 3.]", "a1F[1.06, -0., 6.]", "a2F[0., -1., 5.]", "a3F[0.02, -0., 4.]", # lowpT bin 00,
    #"a0F[2.03, -0., 4.]", "a1F[2.06, -0., 6.]", "a2F[0., -1., 5.]", "a3F[0.02, -0., 4.]", # lowpT bin 01, 02
    #"a0F[50.03, -100., 100.]", "a1F[8.06, 0., 10.]", "a2F[0.03, -0., 1.]", "a3F[0.02, 0., 1.]", # lowpT bin 04
    
    #"a0F[12., 2., 15.]", "a1F[1.5, 0., 3.]", "a2F[2., -0., 5.]", "a3F[0.3, -0., 3.]", # 2024 ID
    #"a0F[10., 1., 15.]", "a1F[2.7, 0., 5.]", "a2F[1.5, -0., 5.]", "a3F[1.3, -0., 3.]", # 2024 ID, bin 10
    #"a0F[1.7, -2., 15.]", "a1F[3.7, -0., 5.]", "a2F[0.5, -0., 5.]", "a3F[1.1., -0., 4.]", # 2024ID bin 10
       
    
    ]
