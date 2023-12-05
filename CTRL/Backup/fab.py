import os, glob

# build the tiff directories in the IMGLIB
##os.chdir(r"C:\Users\PC\Documents\VPconvert\ORSO\vipp\imglib")
##
with open(r"c:\formab\ctrl\dir_list.txt", 'r', encoding='utf-8', errors='ignore') as f:
    items = f.readlines()
    for i in items:
        os.mkdir(i.strip())
        

##IMGLIB = r"C:\Users\PC\Documents\VPconvert\ORSO\vipp\imglib"
##tiff_removed = set()
##with open(r"C:\FORMAB\CTRL\vipp_tiff_list.txt", 'r') as f:
##    items = f.readlines()
##    for i in items:
##        tiff_removed.add(i.strip())
##    
##
##os.chdir(IMGLIB)
##flist = glob.glob('*.tif')
##for i in flist:
##    if i in tiff_removed:
##        os.remove(i)
##        print 'Removed', i
##
##
##tiff_removed = set()
##with open(r"C:\FORMAB\CTRL\dup_vipp_tiff_list.txt", 'r') as f:
##    items = f.readlines()
##    for i in items:
##        tiff_removed.add(i.strip())
##    
##os.chdir(IMGLIB)
##flist = glob.glob('*.tif')
##for i in flist:
##    if i in tiff_removed:
##        os.remove(i)
##        print 'Removed', i
##
      
        

         

