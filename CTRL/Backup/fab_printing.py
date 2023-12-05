'''
Date:       2021-05-27

Date:       20210715
Update:     - migrate to Python V3.8.10 (64-bits) from V2.7.x (32-bits)
'''

import os,glob,sys,subprocess
from shutil import copyfile


def showmenu1():
    subprocess.call(["cls"], shell=True)
    print(star*65)
    print("\n*** FORMAB Printing ***\n\n")
    print("\t What is the product type?\n")
    print("\t '1' --- > PPP\n")
    print("\t '2' --- > CPF\n")
    print("\t '3' --- > DB\n")
    print("\t '4' --- > DC\n\n")
    print("\t 'Q' --- > Quit the program\n")
    print(star*65)

def showmenu2():
    subprocess.call(["cls"], shell=True)
    print(star*65)
    print("\n*** TIFF Conversion for FORMAB ***\n\n")
    print("Press ANY KEY to continue when the system has finished with the conversion.\n")
    print(star*65)   


def copy_tiff(tiff_loc, wk_dir):
    '''
    copy the tiff files from source to IMGLIB
    '''
    os.chdir(tiff_loc)
    tifffiles = glob.glob('*.tif')
    if tifffiles:
        print('\n')
        for tiff_file in tifffiles:
            copyfile(tiff_file, wk_dir + tiff_file)
            print('Copying ' + tiff_file + ' --- > IMGLIB.')
            #os.remove(tiff_file)
        print ('\n')
    return

def clear_tiff(src):
    tiff_removed = set()
    with open(r"C:\FORMAB\CTRL\clear_tiff_list.txt", 'r', encoding='utf-8', errors='ignore') as f:
        items = f.readlines()
        for i in items:
            tiff_removed.add(i.strip())

    os.chdir(src)
    flist = glob.glob('*.tif')
    for i in flist:
        if i in tiff_removed:
            os.remove(i)
            print('Removed', i)
    return

    
def create_ps(src, dst):
    os.chdir(src)
    vippfiles = glob.glob('*.dat')
    if vippfiles:
        for vipp in vippfiles:
            copyfile(vipp, dst+vipp)
            print('Processing ... ' + vipp)
            os.remove(vipp)
    return

# Main program start here
star = "*"
input_dir = "C:\\FORMAB\\INPUT\\"
vpc_input = "C:\\VPC\\ORSO\input\\ps\\"
IMGLIB = "C:\\VPC\\ORSO\\vipp\\imglib\\"
formab_tiff_dir = "C:\\FORMAB\\TIFF_LOC\\"

pd = {'1':'PPP\\', '2':'CPF\\', '3':'DB\\', '4':'DC\\'}


while True:
    showmenu1()
    mode = input("\tSelect: ")
    if mode.lower() not in ('1', '2', '3', '4', 'q'):
        print ("\n\tInvalid Choice !!!\n")
    else:                           # valid option
        if mode.lower() == 'q':
            sys.exit()
        else:
            clear_tiff(IMGLIB)
            pd_tiff_dir = formab_tiff_dir+pd[mode]
            copy_tiff(pd_tiff_dir, IMGLIB)
            create_ps(input_dir, vpc_input)
            subprocess.call("pause", shell=True)
