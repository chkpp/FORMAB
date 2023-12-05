'''
Date:       2021-05-27

Date:       20210715
Update:     - migrate to Python V3.8.10 (64-bits) from V2.7.x (32-bits)
'''

import os,glob,sys,subprocess
from shutil import copyfile
import time


def showmenu1():
    subprocess.call(["cls"], shell=True)
    print(star*65)
    print("\n*** TIFF Conversion for FORMAB ***\n\n")
    print("\tWhat is the product type?\n")
    print("\t'1' --- > PPP\n")
    print("\t'2' --- > CPF\n")
    print("\t'3' --- > DB\n")
    print("\t'4' --- > DC\n\n")   
    print("\t'Q' --- > Quit the program\n")
    print(star*65)

def showmenu2():
    subprocess.call(["cls"], shell=True)
    print(star*65)
    print("\n*** TIFF Conversion for FORMAB ***\n\n")
    print("Press ANY KEY to continue when the system has finished with the conversion.\n")
    print(star*65)

    
def mapping(inf):
    tmp_list = []
    with open(inf, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tmp_list.append(line)
    return tmp_list


def build_folderlist(inf):
    tmp_list = []
    with open(inf, 'r') as f:
        for line in f:
            tmp_list.append(line.strip())
    return tmp_list


def convert_tiff(src, dst):
    os.chdir(src)
    pdffiles = glob.glob('*.pdf')
    if pdffiles:
        for pdf in pdffiles:
            copyfile(pdf, dst+pdf)
            os.remove(pdf)


def manage_tiff(wk_dir, fd_list, process_list, tiff_loc, fm_dict, process_dict):
    '''
    copy and rename tiff files from DECOMP service to Tiff Location
    
    '''
    for folder in process_dict:
        #os.chdir(wk_dir + folder)
        tifffiles = glob.glob('*.tif')
        print(f'DFD total files: {tifffiles}')
        if tifffiles:  
            print('Now Processing ... ' + folder)
            for tiff_file in tifffiles:
                copyfile(tiff_file, tiff_loc + process_dict[tiff_file])
#                os.remove(tiff_file)

##    for folder in fd_list:
##        os.chdir(wk_dir + folder)
##        tifffiles = glob.glob('*.tif')
##        print(f'FD total files: {tifffiles}')
##        if tifffiles:  
##            print('Processing ... ' + folder)
##            for tiff_file in tifffiles:
##                copyfile(tiff_file, tiff_loc + fm_dict[tiff_file])
###                os.remove(tiff_file)
    subprocess.call('pause', shell=True)
    return


# Main program start here
star = "*"
vpc_input = "C:\\VPC\\FORMAB\input\\ps\\"
IMGLIB = "C:\\VPC\\ORSO\\vipp\\imglib\\"
#IMGLIB = "C:\\FAB\\"


formab_tiff_dir = "C:\\FORMAB\\TIFF_LOC\\"
pdf_input = "C:\\FORMAB\\PDF_INPUT\\"

vipp_tiff = mapping('vipp_tiff_list.txt')
decomp_tiff = mapping('decomp_tiff_list.txt')

dup_vipp_tiff = mapping('dup_vipp_tiff_list.txt')
db_decomp_tiff = mapping('db_decomp_tiff_list.txt')
dc_decomp_tiff = mapping('dc_decomp_tiff_list_new.txt')

file_match = dict(zip(decomp_tiff, vipp_tiff))
db_match = dict(zip(db_decomp_tiff, dup_vipp_tiff))
dc_match = dict(zip(dup_vipp_tiff,dc_decomp_tiff))

folderlist = build_folderlist('dir_list.txt')
db_folderlist = build_folderlist('db_dir_list.txt')
dc_folderlist = build_folderlist('dc_dir_list_new.txt')

pd = {'1':'PPP\\', '2':'CPF\\', '3':'DB\\', '4':'DC\\'}

while True:
#    showmenu1()
#    mode = input("\tSelect: ")
    mode = '4'
    if mode.lower() not in ('1', '2', '3', '4', 'q'):
        print("\n\tInvalid Choice !!!\n")
    else:                           # valid option
        if mode.lower() == 'q':
            sys.exit()
        else:
#            convert_tiff(pdf_input, vpc_input)
            pd_tiff_dir = formab_tiff_dir+pd[mode]
#            time.sleep(60)
#            showmenu2()
#            subprocess.call("pause", shell=True)
#            manage_tiff(IMGLIB, folderlist, dup_folderlist, formab_tiff_dir, file_match, dup_match)
            if mode == '3':
                manage_tiff(IMGLIB, folderlist, db_folderlist, pd_tiff_dir, file_match, db_match)
            else:
                manage_tiff(IMGLIB, folderlist, dc_folderlist, pd_tiff_dir, file_match, dc_match)

#    subprocess.call('pause', shell=True)
