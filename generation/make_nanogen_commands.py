import os

# Read the file list
file_list = []
with open('filelist.txt', 'r') as file:
    file_list = [line.strip() for line in file.readlines()]

# Create the shell script file
sh_file = 'nanogen_commands.sh'
with open(sh_file, 'w') as commandfile:
    
    # Generate commands for each file in the list
    for file_path in file_list:
        commandfile.write(f"cmsRun {file_path} \n")
