'''
    Date: 2018-11-16
    Function: This program will check the existence of tiff file and rename it accordingly and then move it to
    the IMGLIB directory 
'''

import os,csv,time,glob,sys,subprocess
from shutil import copyfile


# Main program start here
# Read the tiff files into dictionary
reader = csv.reader(open('tiff_list.csv', 'r'))
file_match = {}
for row in reader:
   k, v = row
   file_match[k] = v


folderlist = []
with open('tiffconv_ini.txt', 'r') as f:
    for line in f:       
        if 'working_dir' in line:
            working_dir = line[12:-1]
        if 'folder' in line:
            folderlist.append(line[12:-1])
  
# Gather the tiff files for processing
for folder in folderlist:
    os.chdir(working_dir+folder)
    tifffiles = glob.glob('*.tif')
    if len(tifffiles) == 0:         # empty folder
        break
    else:
        print('Processing ... '+folder) 
        for tiff_file in tifffiles:
            #print(file_match[tiff_file])
            copyfile(tiff_file, working_dir+file_match[tiff_file])
            os.remove(tiff_file)

print('\n')
cmd = "pause"
subprocess.call(cmd, shell=True)
sys.exit()



