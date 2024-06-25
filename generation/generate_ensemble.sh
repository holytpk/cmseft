#!/bin/bash
export BASE=$PWD

# Check if cfg_files directory exists, if not, create it
if [ ! -d "$BASE/cfg_files" ]; then
    mkdir cfg_files
fi

if [ ! -d "$BASE/nanogen_files" ]; then
    mkdir nanogen_files
fi

for i in {1..200}; do
    output_file="$BASE/cfg_files/nanogen_TT01j2lCARef_ensemble${i}_cfg.py"
    cmsDriver.py Configuration/GenProduction/python/pythia_fragment.py --python_filename "$output_file" --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --fileout "$BASE/nanogen_files/nanogen_TT01j2lCARef_${i}.root" --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 15000 --customise_commands "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123;process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable)"
done
