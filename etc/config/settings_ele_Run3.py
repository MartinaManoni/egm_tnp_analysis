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
    'passingMVASummer18ULwpHZZ_sipdzdxy' : '(passingMVASummer18ULwpHZZ == 1 && fabs(el_sip) < 4 && fabs(el_dz) < 1 && fabs(el_dxy) < 0.5)',#Andro 2022 with UL18 training
    }

baseOutDir = '/eos/user/m/mmanoni/Tnp_results/hzzWinter22/newBinning_2023preBPixResults_sipdzdxy_el3charge_cut60'

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

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Run3_2022['data_Run2022G'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_Andro['data_Run3D'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_Andro['data_Run3E'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_Andro['data_Run3F'] )
#samplesDef['data'].add_sample( tnpSamples.Run3_Andro['data_Run3G'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
#if not samplesDef['tagSel'] is None:
    #samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    #samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut


## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_data_Run2022_B-G.totWeight'
# TODO: verify these MC weights are correct
weightName = 'weights_data_Run2022_inclusive.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_miniAOD/DY_amcatnloext_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')

#############################################################
########## bining definition  [can be nD bining]
#############################################################
# Based on Andro binning 
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.0, -1.566, -1.444, -0.8, 0, 0.8, 1.444, 1.566, 2.0, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 15, 20, 35, 50, 100, 500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'

#&& el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60
#el_3charge==1
additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    1 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    2 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    3 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    4 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    5 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    6 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    7 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    8 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    9 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    #12 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
    #17 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60',
}

#transverse mass cut (WW)

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
   
   # "{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.1,0.1],a3[0, -0.5, 0.5]}", #2023 preBPix: works for bin 2/3/4/5 (bins 0-7) 
   # "{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0, -0.01, 0.01],a3[0, -0.05, 0.05]}", #2023 preBPix: works for 6/7 - used for 0/1 but not the best (bins 8-9)
    ]

    #"{a0[-0.9,-1.5,-0.5],a1[0.2,0.,0.5],a2[0.,-0.5,0.5]}",
    #"{a0[-0.9,-1.5,-0.5],a1[0.1,-0.5,0.5],a2[0.,-0.01,0.01], a3[0, -0.05, 0.05]}", #bin 2/6/5
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.5,0.5], a3[0, -0.5, 0.5]}",

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    #"meanP[-0.0,-5.0,5.0]","sigmaP[5,0.7,10.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]", #2023 preBPix: bin27
    #"meanF[-8.0,-20.0,10.0]","sigmaF[5,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[5,-5,7]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,30.0]", #2023 preBPix: bin27
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]", 
    #"acmsF[60.,55.,75.]","betaF[0.055,0.001,0.1]","gammaF[0.22, 0.005, 1]","peakF[90.0]", #2023 preBPix: (new binning 40/41/43/44/45/46/48)
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.12,0.12],a3[0, -0.5, 0.5]}", #2023 preBPix: 0, 2-9 Chebychev
    #"{a0[-0.9,-2,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.2,0.2],a3[0, -0.1, 0.1]}", #2023 preBPix: 1 Chebychev
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "a0[2,0.5,7.5]","a1[2,1,40.7]","a2[7,2,62]",  #2023 preBPix: Gamma bin 1/6/7 + bin 11
    #"a0[2,0.5,7.5]","a1[7.5,6,40.7]","a2[15,10,62]", #2023 preBPix: Gamma bin 0/2/3/4/5
    #"alphaF[-0.0,-0.5.,0.5]",
    #"alphaF[-0.010,-0.010,-0.0]",#2023 preBPix: For the rest of the bins use this "alphaF[-0.0,-0.5.,0.5]",
    ]

tnpParAltSigBkgFit = [
    "meanP[-2.08,-3.,2.]","sigmaP[1,0.7,6.0]","alphaP[2.0,0.0,2.0]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1.487,0.,3.]",
    "meanF[-2.195,-3.0,-1.0]","sigmaF[4.786,3.,6.]","alphaF[0.72,0,1.5]",'nF[1.734,1.0,2.5]',"sigmaF_2[2.0,1.0,3.0]","sosF[2.0,1.0,3.0]", #bins 0,1,2,5,6,7
    "alphaP_2[0.,-5.,5.]",
    #"alphaF_2[0,-1, 1]",
    "a0[2,0.5,7.5]","a1[30,1,40.7]","a2[10,2,62]",  #2023 preBPix: Gamma bin 2
    #"a0[2,0.5,7.5]","a1[7.5,6,40.7]","a2[5,10,30]", #2023 preBPix: Gamma bin 0/1/3/4/7
    #"a0[2,0.5,7.5]","a1[30,1,40.7]","a2[20,2,62]", #2023 preBPix: Gamma bin 6
]

     #2023 preBPix:: use Chebychev only for bin 0/1/3/4/5 # "{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.05,0.05],a3[0, -0.5, 0.5]}"
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.1,0.1],a3[0, -0.5, 0.5]}",#2023 preBPix: only bin 2/10/11/
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.06,0.06],a3[0, -0.1, 0.1]}", #2023 preBPix:: use Chebychev only for bin 6
                    #"{a0[-0.9,-1.5,-0.2],a1[0.,-0.1,0.1],a2[0.,-0.9,0.9],a3[0, -1.5, 1.5]}", #2023 preBPix:: use this Chebychev only for bin 17/19/20/23

    #"meanF[-0.974,-1.3,-0.9]","sigmaF[4.668,4.2,5.2]","alphaF[1.376,0.8,2.0]",'nF[0.236,0.1,0.4]',"sigmaF_2[2.0]","sosF[2.0]", 
    #"meanF[-2.195,-3.0,-0.0]","sigmaF[4.786,3.,6.]","alphaF[0.72,0,3.5]",'nF[1.734,1.0,2.5]',"sigmaF_2[2.0,1.0,3.0]","sosF[2.0,0.4,3.0]", #bins 3,4
    #"meanF[-2.754,-3.5,0.0]","sigmaF[3.871,3.2,4.6]","alphaF[1.873,1.0,2.8]",'nF[0.163]',"sigmaF_2[2.0]","sosF[2.863,0.0,3.7]", #bins 8,9 14,15
    #"meanF[-0.155,-0.2,-0.1]","sigmaF[0.702,0.4,1.0]","alphaF[1.116,1.0,1.3]",'nF[0.77,0.0.1.5]',"sigmaF_2[2.0,1.5,2.5]","sosF[1.477,1.2,1.7]", #bins 10,13
    #"meanF[-2.754,-3.5,0.0]","sigmaF[2.4,2.0,3.5]","alphaF[1.873,1.0,2.8]",'nF[0.071,0,0.2]',"sigmaF_2[2.0]","sosF[2.6,0.0,3.7]", #bins 8,9, 14,15,11,12
    #"meanF[-2.754,-3.5,0.0]","sigmaF[2.4,2.0,3.5]","alphaF[1.873,1.0,2.8]",'nF[0.071,0,0.2]',"sigmaF_2[2.0]","sosF[2.6,0.0,3.7]", #bins 8,9, 14,15,11,12
    #"meanF[-2.754,-3.5,1.0]","sigmaF[2.4,2.0,3.5]","alphaF[1.873,1.0,6.8]",'nF[0.071,0,0.2]',"sigmaF_2[2.0]","sosF[2.6,0.0,3.7]", #bins 16-23
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",

    #"meanP[-1.3,-1.4,-0.2]","sigmaP[1,0.1,3.0]","alphaP[1.2,1.0,5.0]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1.4,1.3,1.5]",
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,0.0,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.1,5.0]", #works for most bins

        #"alpha2F[-0.033,-0.036,-0.03]", #bins 10,13
    #"alpha2F[-0.028,-0.1,0.0]", #bins 8,9,14,15
    #"a0[1.87,1.7,7.5]","a1[14.7,13.7,15.7]","a2[30,28,62]",
    #"a0[2.0,1.9,2.4]","a1[15.7,13.7,18.7]","a2[30,28,62]", #bins 11,12
    #"a0[0.25,0.1,0.35]","a1[140,135,160]","a2[40,35,75]", #bins 0,1,6,7
    #"a0[0.1,0.01,0.5]","a1[120,80,160]","a2[41.829,36,48]",
    #"a0[0.25,0.1,0.35]","a1[70,60,80]","a2[37,35,75]", #bins 2,5
    #"a0[1.7,1.0,2.5]","a1[15.7,12.7,18.7]","a2[32,20,44]", #bins 3,4
    #"a0[1.87,1.7,7.5]","a1[15.7,14.7,40.7]","a2[30,28,62]",
    #"a0[1.3,1.2,1.45]","a1[21.7,20.7,29.7]","a2[55.6,51.6,57.6]", #bins 16-23