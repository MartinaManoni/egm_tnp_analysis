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

baseOutDir = '/eos/user/m/mmanoni/Tnp_results_2023postBPix_NO_HOLE_REGION/hzzSummer18UL/2023preBPixResults_sipdzdxy_el3charge_cut60'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Run3_2023['data_Run2023D'].clone(),
    'mcNom'  : tnpSamples.Run3_2023['DYpostBPix'].clone(),
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

weightName = 'weights_data_Run2023D.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/tnpTuples/Prompt2023/pileupReweightingFiles/postBPIX/DY_amcatnloext_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/tnpTuples/Prompt2023/pileupReweightingFiles/preBPIX/DY_madgraph_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/ec/tnpTuples/Prompt2023/pileupReweightingFiles/preBPIX/DY_amcatnloext_ele.pu.puTree.root')


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
### cut with HOLE EXCLUDED 
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && ( (el_sc_eta>=0 || el_sc_eta<= -1.5) || (el_sc_eta<0 && el_sc_eta>-1.5 && (el_phi>-0.8 || el_phi<-1.2)))'

#&& el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60
#el_3charge==1
additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    1 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    2 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    3 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    4 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    5 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    6 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    7 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    8 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
    9 : 'tag_Ele_pt > 50 && el_3charge==1 && sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) <  60',
}

#transverse mass cut (WW)

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    #"meanP[-0.0,-2.0,2.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]", 
    #"meanP[-0.0,-2.0,2.0]","sigmaP[4.5,4.,6.0]", #bin2/7
    "meanP[-0.0,-2.0,2.0]","sigmaP[2.,2.,3.0]", #bin 12
    "meanF[-0.0,-5.0,5.0]","sigmaF[2.,2.,3.0]", #bin 2/7
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.5, -2, 2]","peakP[90.0]",
    #"acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.5, -2, 2]","peakF[90.0]",
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.022,-0.02],a3[0, -0.02, 0.02]}", #bin 2/7

    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.019,-0.02],a3[0, -0.02, 0.02]}", #bin 12

    #"{a0[-0.9,-1.5,-0.1],a1[0.,-0.5,0.5],a2[0.,-0.5,-0.02],a3[0, -0.02, 0.02]}", #bin 12
    "{a0[-0.9,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}"

    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.05,0.05],a3[0, -0.02, 0.02]}", #bin 1/2/3/4/5/6/7
    ]

#general

tnpParAltSigFit = [
    "meanP[-0.0,-2.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]", #"meanP[-0.0,-4.0,5.0] bin 1
    "meanF[-0.0,-3.0,5.0]","sigmaF[0.5,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.04]","gammaP[0.1, 0.005, 1.0]","peakP[90.0]", #bin 22/27 betaP[0.04,0.01,0.2]
    #"acmsF[40.,50.,90.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1.0]","peakF[90.0]", # bin 8 betaF[0.04,0.01,0.08] bin 9 betaF[0.04,0.01,0.09]" --- bin 40/41/49  "acmsF[40.,50.,90.]",
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.05,0.05],a3[0, -0.1, 0.1]}", #bin 0/2/3
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.02,-0.019],a3[0, -0.1, 0.1]}", #bin 2
    #"{a0[-0.9,-1.5,-0.5],a1[0.,-0.5,0.5],a2[0.,-0.05,0.05],a3[0, -0.5, 0.5]}", #bin 0-7/15

    #"{a0[-0.9,-1.5,-0.1],a1[0.,-0.5,0.5],a2[0.,-0.5,-0.02],a3[0, -0.02, 0.02]}", #bin 12/14
    "{a0[-0.9,-1.5,-0.2],a1[0.,-0.5,0.5],a2[0.,-0.09,0.09],a3[0, -0.5, 0.5]}" #24/25/28
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]", #"meanP[-0.5,-5.0,5.0]","sigmaP[0.9,0.5,5.0]", bin 28
    #"meanP[-0.5,-5.0,5.0]","sigmaP[0.9,0.5,5.0]", #bin 28
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    #"alphaF[0.,-5.,5.]",
    #"a0[2,0.5,7.5]","a1[7.5,6,40.7]","a2[15,10,60]", #2023 postPix: Gamma bin 1/3/4/5/6/
    #"a0[0.9, 0.7, 2.0]","a1[40,35,50]","a2[58,50,60]", #2023 preBPix: Gamma bin 7
    #"a0[0.9, 0.7, 2.0]","a1[40,35,50]","a2[58,10,60]",# #2023 preBPix: Gamma bin 2
    
    #"a0[2,0.5,7.5]","a1[2,10,40]","a2[7,2,60]", 
    "a0[1.5, 1.4, 1.6]","a1[7.5,6,40.7]","a2[15,10,62]", #bin 14/15
    #"a0[2,0.5,7.5]","a1[7.5,6,40.7]","a2[15,10,62]",#24/25
    #"a0[2,1.9,2.1]","a1[7.5,6,40.7]","a2[15,10,62]",#28

    #"alphaF[-0.0,-0.5.,0.5]",
    #"alphaF[-0.010,-0.010,-0.0]",#2023 preBPix: For the rest of the bins use this "alphaF[-0.0,-0.5.,0.5]",
    ]

tnpParAltSigBkgFit = [
    "meanP[-2.08,-3.,2.]","sigmaP[1,0.7,6.0]","alphaP[2.0,0.0,2.0]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1.487,0.,3.]",
    "meanF[-2.195,-3.0,-1.0]","sigmaF[4.786,3.,6.]","alphaF[0.72,0,5.0]",'nF[1.734,1.0,2.5]',"sigmaF_2[2.0,1.0,3.0]","sosF[2.0,1.0,3.0]", #bin 23 alphaF[0.72,0,5.0]
    "alphaP_2[0.,-5.,5.]",
    #"alphaF_2[0,-5., +5.]",
    
    #"a0[2,0.05,10]","a1[7.5,4,40.7]","a2[5,10,80]", #2023 postBPix: 1/2/3/4/
    #"a0[2,0.1,10]","a1[7.5,4,40.7]","a2[5,10,70]"# bin 5
    #"a0[2,0.1,7.5]","a1[7.5,4,40.7]","a2[5,10,70]",#bin 2/3
   # "a0[2,0.1,7.5]","a1[7.5,4,40.7]","a2[5,10,65]" #bin 6 
    #"a0[2,0.05,10]","a1[7.5,4,20]","a2[5,10,30]",#bin 7 
    #"a0[1.5, 1.4, 1.6]","a1[7.5,6,40.7]","a2[15,10,62]", #bin 14/15
    #"a0[2,0.5,7.5]","a1[7.5,6,40.7]","a2[15,10,62]",#25
    "a0[2,1.9,2.1]","a1[7.5,6,40.7]","a2[15,10,62]",#24
]
