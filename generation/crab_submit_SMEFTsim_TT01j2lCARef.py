from CRABClient.UserUtilities import config#, getUsername
config = config()

config.General.requestName = 'TT01j2lCARef'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'nanogen_TT01j2lCARef_cfg.py'
config.JobType.maxMemoryMB = 1000
config.JobType.inputFiles = ['nanogen_TT01j2lCARef.sh', 'nanogen_TT01j2lCARef_cfg.py']
config.JobType.scriptExe = 'nanogen_TT01j2lCARef.sh'
config.JobType.allowUndistributedCMSSW=True

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 1000000
#config.Data.splitting = 'Automatic'
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/lingqian/cmseft/dileptonic/' #% (getUsernameFromCRIC())
config.Data.outputPrimaryDataset = 'SMEFTsim_topU3l_MwScheme_UFO_TT01j2lCARef'
config.Data.outputDatasetTag = '106X_mc2017_realistic_v6_Realistic25ns13TeVEarly2017Collision'

config.Site.storageSite = 'T2_US_Purdue'

config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
