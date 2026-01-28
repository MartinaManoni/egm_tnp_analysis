
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
baseOutDir = '/eos/user/m/mmanoni/Tnp_results_2024_GAPREGION/hzzWinter22/2024Results/'
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
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-1.566,-1.4442, 1.4442, 1.566] }, # GAP REGION
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 20] }, # GAP REGION
]
#############################################################
########## Cuts definition for all samples
#############################################################
cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && tag_Ele_Iso122X > 0.9 && el_q*tag_Ele_q < 0'

additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    1 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
    2 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 ',
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
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-1.0,1.0],a3[0, -0.5, 0.5]}" #bin 7/13/14/15/16

    "{a0[-0.9,-1.5,-0.5],a1[0.,-0.25,0.25],a2[0.,-1.0,1.0],a3[0, -0.5, 0.5]}"
    ]

tnpParAltSigFit = [
    #SIGN
    #sigmaP[15.0,15.0,20.0
    "meanP[-0.0,-5.0,5.0]","sigmaP[1.,0.,10.0]","alphaP[2.0,1.0,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]", 
    "meanF[-0.0,-5.0,5.0]","sigmaF[1.,0.,15.0]","alphaF[2.5,1.0,3.0]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.,8.0]",

    # --CMSShape BKG
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1.]","peakP[90.0]",
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.05,0.05],a3[0, -0.2, 0.2]}", #bin 0-1
    "{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.02,0.02],a3[0, -0.05, 0.05]}", #bin 2

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
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    # --- Exponential ALL
    "alphaP[0.,-5.,5.]",
    # --- Bernstein LOW PT
    #"a0[12., 0.9., 15.]", "a1[2., 0., 1.]", "a2[0.1, -0., 0.5]", "a3[0.3, -0., 3.]",  #bin 0-1
    "a0[12., 0.9., 15.]", "a1[2., 0., 0.5]", "a2[0.1, -0., 0.2]", "a3[0.3, -0., 3.]",  #bin 2
    ]

tnpParAltSigBkgFit = [

    "meanP[-0.5,-5.0,5.0]","sigmaP[3,0.7,6.0]","alphaP[0.5,0.,5.5]" ,'nP[2,-5,5]',"sigmaP_2[0.1,0.,6.0]","sosP[0.02,0.,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[5.,5.,20.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",

    # --- Exponential
    "alphaP_2[0.,-5.,5.]",
    #"alphaF_2[0.,-5.,5.]",
    #"a0[5., 1., 20.]", "a1[2., 0., 3.]", "a2[0.2, -0., 0.5]", "a3[0.3, -0., 3.]", #bin 0-1
    "a0[5., 1., 30.]", "a1[2., 0., 2.]", "a2[0.2, -0.2, 0.2]", "a3[0.3, -0.6, 3.]",
    ]