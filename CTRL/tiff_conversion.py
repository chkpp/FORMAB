'''
Date:       2021-05-27

Date:       20210715
Update:     - migrate to Python V3.8.10 (64-bits) from V2.7.x (32-bits)

Revised Date: 03122022
'''

import os,glob,sys,subprocess
from shutil import copyfile, rmtree
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


def manage_tiff(wk_dir, process_list, tiff_loc, process_dict):
    '''
    copy and rename tiff files from DECOMP service to Tiff Location
    
    '''
    rmtree(tiff_loc)
    os.mkdir(tiff_loc)
    for folder in process_list:
        os.chdir(wk_dir + folder)
        tifffiles = glob.glob('*.tif')
        if tifffiles:  
            print('Now Processing ... ' + folder)
            for tiff_file in tifffiles:
#                os.remove(tiff_loc + tiff_file)
                copyfile(tiff_file, tiff_loc + tiff_file)
    subprocess.call('pause', shell=True)
    return


# Main program start here
star = "*"
vpc_input = "C:\\VPC\\FORMAB\input\\ps\\"
IMGLIB = "C:\\VPC\\ORSO\\vipp\\imglib\\"

formab_tiff_dir = "C:\\FORMAB\\TIFF_LOC\\"
pdf_input = "C:\\FORMAB\\PDF_INPUT\\"

db_decomp = mapping('db_decomp.txt')
dc_decomp = mapping('dc_decomp.txt')
cpf_decomp = mapping('cpf_decomp.txt')
ppp_decomp = mapping('ppp_decomp.txt')

db_vipp = mapping('db_vipp.txt')
dc_vipp = mapping('dc_vipp.txt')
cpf_vipp = mapping('cpf_vipp.txt')
ppp_vipp = mapping('ppp_vipp.txt')

##db_dict = dict(zip(db_vipp, db_decomp))
##dc_dict = dict(zip(dc_vipp, dc_decomp))
##cpf_dict = dict(zip(cpf_vipp, cpf_decomp))
##ppp_dict = dict(zip(ppp_vipp, ppp_decomp))

db_dict = dict(zip(db_decomp, db_vipp))
dc_dict = dict(zip(dc_decomp, dc_vipp))
cpf_dict = dict(zip(cpf_decomp, cpf_vipp))
ppp_dict = dict(zip(ppp_decomp, ppp_vipp))

db_folder = mapping('db_dir.txt')
dc_folder = mapping('dc_dir.txt')
cpf_folder = mapping('cpf_dir.txt')
ppp_folder = mapping('ppp_dir.txt')

pd = {'1':'PPP\\', '2':'CPF\\', '3':'DB\\', '4':'DC\\'}
dict_sel = {'1':(ppp_dict, ppp_folder), '2':(cpf_dict, cpf_folder), '3':(db_dict, db_folder), '4':(dc_dict, dc_folder)}

while True:
    showmenu1()
    mode = input("\tSelect: ")
    if mode.lower() not in ('1', '2', '3', '4', 'q'):
        print("\n\tInvalid Choice !!!\n")
    else:                           # valid option
        if mode.lower() == 'q':
            sys.exit()
        else:
            convert_tiff(pdf_input, vpc_input)
            pd_tiff_dir = formab_tiff_dir+pd[mode]
            showmenu2()
            subprocess.call("pause", shell=True)
            manage_tiff(IMGLIB, dict_sel[mode][1], pd_tiff_dir, dict_sel[mode][0])

#    subprocess.call('pause', shell=True)
