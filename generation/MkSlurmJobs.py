#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("commandlist")
parser.add_argument("--cpu", type=str, default="1", help='Number of cpus requested for this job. Default 1.')
parser.add_argument("--mem", type=str, default="32000", help='Amount of memory to allocate per cpu for this job. Default 32000.')
parser.add_argument("--time", type=str, default="40:00:00", help='Amount of time to submit job for. Default is 4 hours.')
args = parser.parse_args()

BASE = str(os.getenv("BASE"))

i = 0

if os.path.exists("cmsSlurmJobs"):
    for job in os.listdir("cmsSlurmJobs"):
        if i < int(job.strip('SlurmJob_').strip('.sh')): 
            i = int(job.strip('SlurmJob_').strip('.sh'))+1

else: os.makedirs("cmsSlurmJobs")

if not os.path.exists("nohuplogs"): os.makedirs("nohuplogs")
if not os.path.exists("plotslogs"): os.makedirs("plotslogs")


commandlistfilepath = args.commandlist
commandlistfile     = open(commandlistfilepath, "r")
lines = commandlistfile.readlines()


runfile = open("RuncmsSlurm_"+os.path.basename(commandlistfilepath).rsplit(".",1)[0]+".sh", "w")

runfile.write("#!/bin/sh")
runfile.write("\n")
runfile.write("source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.6/current/el7-x86_64/setup.sh")
runfile.write("\n")
runfile.write("export X509_USER_PROXY=~/x509up_u`id -u`")
runfile.write("\n")
runfile.write("voms-proxy-init -voms cms -rfc -valid 168:00")
runfile.write("\n")

for line in lines :
    if len(str(line.strip())) == 0: continue
    if str(line)[0] == "#": continue
    if str(line) == "\n": continue

    i   += 1
    line = line.strip("\n")
    sh_file = "cmsSlurmJobs/SlurmJob_" + str(i) + ".sh"
    
    with open(sh_file, "w") as cfg :
        cfg.write("#!/bin/sh")
        cfg.write("\n")
        cfg.write("#SBATCH -A cms -p hammer-nodes")
        #cfg.write("#SBATCH -A physics")
        cfg.write("\n")
        cfg.write("#SBATCH --ntasks=1")
        cfg.write("\n")
        cfg.write("#SBATCH --cpus-per-task=" + str(args.cpu))
        #cfg.write("#SBATCH --cpus-per-task=1")
        cfg.write("\n")
        cfg.write("#SBATCH --mem-per-cpu=" + str(args.mem))
        #cfg.write("#SBATCH --mem-per-cpu=8000")
        cfg.write("\n")
        cfg.write("#SBATCH --time=" + str(args.time))
        #cfg.write("#SBATCH --time=3:59:00")
        cfg.write("\n")
        cfg.write("cd " + BASE)
        cfg.write("\n")
        cfg.write(f"source {BASE}/install_cmssw_10_6_27.sh")
        cfg.write("\n")        
        cfg.write("echo \'"+str(line)+"\'")
        cfg.write("\n")
        cfg.write(str(line))


    runfile.write("sbatch cmsSlurmJobs/SlurmJob_" + str(i) + ".sh")
    runfile.write("\n")


