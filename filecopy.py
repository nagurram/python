# import OS module
import os
import shutil

# Get the list of all files and directories
path = "F://Prasanthi Phone Photos"
dpath = "F://phone Photos"
for f in os.listdir(path):
    # print(path+'//'+f)
    for f2 in os.listdir(path+'//'+f):
      shutil.copyfile(path+'//'+f+'//'+f2, dpath+'//'+f2)
