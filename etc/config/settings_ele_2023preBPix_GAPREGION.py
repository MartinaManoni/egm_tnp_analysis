#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passingCutBasedVeto94XV2'    : '(passingCutBasedVeto94XV2   == 1)',
    'passingCutBasedLoose94XV2'   : '(passingCutBasedLoose94XV2  == 1)',
    'passingCutBasedMedium94XV2'  : '(passingCutBasedMedium94XV2 == 1)',
    'passingCutBasedTight94XV2'   : '(passingCutBasedTight94XV2  == 1)',
    'passingMVA94Xwp80isoV2' : '(passingMVA94Xwp80isoV2 == 1)',
    'passingMVA94Xwp90isoV2' : '(passingMVA94Xwp90isoV2 == 1)',
    'passingMVA94Xwp80noisoV2' : '(passingMVA94Xwp80noisoV2 == 1)',
    'passingMVA94Xwp90noisoV2' : '(passingMVA94Xwp90noisoV2 == 1)',
    'passingMVA94XwpLisoV2'    : '(passingMVA94XwpLisoV2 == 1)',
    'passingMVA94XwpLnoisoV2'  : '(passingMVA94XwpLnoisoV2 == 1)',
    'passingMVA94XwpHZZisoV2'  : '(passingMVA94XwpHZZisoV2 == 1)',
    'passingMVAhzzWinter22'  : '(passingMVAhzzWinter22 == 1 && fabs(el_sip) < 4 && fabs(el_dz) < 1 && fabs(el_dxy) < 0.5)', #Martina new ID hzzWinter22 with 22 training
    'passingMVASummer18ULwpHZZ_sipdzdxy' : '(passingMVASummer18ULwpHZZ == 1 && fabs(el_sip) < 4 && fabs(el_dz) < 1 && fabs(el_dxy) < 0.5)',#Using this 
    }

baseOutDir = '/eos/user/m/mmanoni/Tnp_results_2023preBPix_GAPREGION/hzzSummer18UL/2023preBPixResults'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Run3_2023['data_Run2023C'].clone(),
    'mcNom'  : tnpSamples.Run3_2023['DYpreBPix'].clone(),
    #'mcAlt'  : tnpSamples.Run3['DY_amcatnloext'].clone(),
    #'tagSel' : tnpSamples.Run3['DY_madgraph'].clone(),
}

samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()

weightName = 'weights_data_Run2023C.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/tnpTuples/Prompt2023/pileupReweightingFiles/preBPIX/DY_amcatnloext_ele.pu.puTree.root')



#############################################################
########## bining definition  [can be nD bining]
#############################################################
# Based on Andro binning 
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-1.566,-1.4442, 0, 1.4442, 1.566] }, # GAP REGION
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 20] }, # GAP REGION
]
#############################################################
########## Cuts definition for all samples
#############################################################
cutBase = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'

additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
    1 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
    2 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
}


#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    #bins 0-2
    "meanP[-0.0,-2.0,2.0]","sigmaP[3.1,2.5,5.0]",  
   #"meanF[-0.0,-2.0,2.0]","sigmaF[2.8,2.5,5.0]",
    "meanF[-0.0,-2.0,2.0]","sigmaF[2.5,2.5,2.6]",

    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.03]","gammaP[0.1, -2, 2]","peakP[90.0]", 

    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}",#bin 2
    "{a0[-0.9,-1.5,-0.5],a1[0.,-0.3,0.3],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}",#bin 0

    ]

tnpParAltSigFit = [
    "meanP[-0.0,-2.0,5.0]","sigmaP[1,7.,10.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-10.0,5.0]","sigmaF[1,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.5,0.5,6.0]","sosF[1,0.5,10.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.001,0.05]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.3,0.3],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}",
    "{a0[-0.9,-1.5,-0.5],a1[0.,-0.2,0.2],a2[0.,-0.05,0.05],a3[0, -0.005, 0.005]}"

    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,3.,70.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,3.0]", #altBkg bin 0
 
    "alphaP[0.,-5.,5.]", #exp
    #"alphaF[0.,-5.,5.]", #exp
    #"a0[2,0.5,7.5]","a1[2,10,40]","a2[7,2,60]", #gamma
    #"a0[2,0.5,10.]","a1[7.5,6,60]","a2[20,10,70]", #bin 2
    "a0[0.7, 0.2, 0.9]","a1[49., 40., 50.]","a2[55., 45., 60.]",
 
    ]

tnpParAltSigBkgFit = [
    "meanP[-2.,-5.,2.]","sigmaP[1,2.,70.0]","alphaP[2.0,0.0,2.0]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,20.0]","sosP[1.487,0.,3.]",
    "meanF[-2.,-5.0,2.]","sigmaF[4.786,0.,6.]","alphaF[0.72,0,5.0]",'nF[1.734,1.0,2.5]',"sigmaF_2[2.0,1.0,3.0]","sosF[2.0,1.0,3.0]", #bin 23 alphaF[0.72,0,5.0]
    "alphaP_2[0.,-5.,5.]",
    "a0[0.9, 0.7, 2.0]","a1[40,35,50]","a2[58,50,60]", #bin 7
]