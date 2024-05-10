# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/GenProduction/python/pythia_fragment.py --python_filename nanogen_TT01j2lCARef_cfg.py --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --fileout file:nanogen_TT01j2lCARef.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 15000 --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123;process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable)
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017

process = cms.Process('NANOGEN',Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('PhysicsTools.NanoAOD.nanogen_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(15000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/pythia_fragment.py nevts:15000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODGENoutput = cms.OutputModule("NanoAODOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:nanogen_TT01j2lCARef.root'),
    outputCommands = process.NANOAODGENEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v6', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings', #extra                            
            'processParameters'
        ),
        processParameters = cms.vstring(
            'JetMatching:setMad = on',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 999.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 30.',
            'JetMatching:nQmatch = 5',
            'JetMatching:nJetMax = 1',
            'JetMatching:doShowerKt = off'
            'SLHA:useDecayTable = off',  # Use pythia8s own decay mode instead of decays defined in LH accord
            '25:onMode = on',       # Allow all higgs decays
            '25:offIfAny = 5 5',    # Switch decays of b quarks off                                                                 

        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:ecmPow=0.03344',
            'MultipartonInteractions:bProfile=2',
            'MultipartonInteractions:pT0Ref=1.41',
            'MultipartonInteractions:coreRadius=0.7634',
            'MultipartonInteractions:coreFraction=0.63',
            'ColourReconnection:range=5.176',
            'SigmaTotal:zeroAXB=off',
            'SpaceShower:alphaSorder=2',
            'SpaceShower:alphaSvalue=0.118',
            'SigmaProcess:alphaSvalue=0.118',
            'SigmaProcess:alphaSorder=2',
            'MultipartonInteractions:alphaSvalue=0.118',
            'MultipartonInteractions:alphaSorder=2',
            'TimeShower:alphaSorder=2',
            'TimeShower:alphaSvalue=0.118',
            'SigmaTotal:mode = 0',
            'SigmaTotal:sigmaEl = 21.89',
            'SigmaTotal:sigmaTot = 100.309',
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2',
            'Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',                                         
        )
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on', 
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,isr_G2GG_muR_up isr:G2GG:muRfac=2.0,isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,isr_X2XG_muR_up isr:X2XG:muRfac=2.0,isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,isr_G2GG_cNS_up isr:G2GG:cNS=2.0,isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,isr_X2XG_cNS_up isr:X2XG:cNS=2.0}', 
            'UncertaintyBands:nFlavQ = 4', 
            'UncertaintyBands:MPIshowers = on', 
            'UncertaintyBands:overSampleFSR = 10.0', 
            'UncertaintyBands:overSampleISR = 10.0', 
            'UncertaintyBands:FSRpTmin2Fac = 20', 
            'UncertaintyBands:ISRpTmin2Fac = 1'
        ) # how is this different?       
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/uscms_data/d3/he614/cmseft/generation/genproductions/bin/MadGraph5_aMCatNLO/TT01j2lCARef_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(15000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.nanoAOD_step = cms.Path(process.nanogenSequence)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODGENoutput_step = cms.EndPath(process.NANOAODGENoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.nanoAOD_step,process.endjob_step,process.NANOAODGENoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
        if path in ['lhe_step']: continue
        getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nanogen_cff
from PhysicsTools.NanoAOD.nanogen_cff import customizeNanoGEN

#call to customisation function customizeNanoGEN imported from PhysicsTools.NanoAOD.nanogen_cff
process = customizeNanoGEN(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123;process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
named_weights = [
"dummy # Name of first argument seems to be rwgt_1. Add dummy to fix it.",
"EFTrwgt0_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt1_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt2_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt3_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt4_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt5_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt6_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt7_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt8_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt9_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt10_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt11_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt12_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt13_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt14_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt15_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt16_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt17_ctGRe_2.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt18_ctGRe_1.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt19_ctGRe_1.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt20_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt21_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt22_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt23_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt24_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt25_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt26_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt27_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt28_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt29_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt30_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt31_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt32_ctGRe_1.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt33_ctGRe_0.0_ctGIm_2.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt34_ctGRe_0.0_ctGIm_1.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt35_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt36_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt37_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt38_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt39_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt40_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt41_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt42_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt43_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt44_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt45_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt46_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt47_ctGRe_0.0_ctGIm_1.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt48_ctGRe_0.0_ctGIm_0.0_cQj18_2.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt49_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt50_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt51_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt52_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt53_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt54_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt55_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt56_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt57_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt58_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt59_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt60_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt61_ctGRe_0.0_ctGIm_0.0_cQj18_1.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt62_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_2.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt63_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt64_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt65_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt66_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt67_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt68_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt69_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt70_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt71_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt72_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt73_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt74_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_1.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt75_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_2.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt76_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt77_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt78_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt79_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt80_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt81_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt82_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt83_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt84_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt85_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt86_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_1.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt87_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_2.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt88_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt89_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt90_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt91_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt92_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt93_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt94_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt95_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt96_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt97_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_1.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt98_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_2.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt99_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt100_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt101_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt102_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt103_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt104_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt105_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt106_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt107_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_1.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt108_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_2.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt109_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt110_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt111_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt112_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt113_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt114_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt115_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt116_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_1.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt117_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_2.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt118_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt119_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt120_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt121_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt122_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt123_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt124_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_1.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt125_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_2.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt126_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt127_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt128_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt129_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt130_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt131_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_1.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt132_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_2.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt133_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt134_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt135_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt136_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt137_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_1.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt138_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_2.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt139_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt140_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt141_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt142_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_1.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt143_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_2.0_ctj1_0.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt144_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_1.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt145_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt146_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_1.0_ctj1_0.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt147_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_2.0_cQu1_0.0_cQd1_0.0",
"EFTrwgt148_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_1.0_cQd1_0.0",
"EFTrwgt149_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_1.0_cQu1_0.0_cQd1_1.0",
"EFTrwgt150_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_2.0_cQd1_0.0",
"EFTrwgt151_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_1.0_cQd1_1.0",
"EFTrwgt152_ctGRe_0.0_ctGIm_0.0_cQj18_0.0_cQj38_0.0_cQj11_0.0_cQj31_0.0_ctu8_0.0_ctd8_0.0_ctj8_0.0_cQu8_0.0_cQd8_0.0_ctu1_0.0_ctd1_0.0_ctj1_0.0_cQu1_0.0_cQd1_2.0",
]
process.genWeightsTable.namedWeightIDs = named_weights
process.genWeightsTable.namedWeightLabels = named_weights
