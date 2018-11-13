from PIL import Image
from shutil import copyfile
import os
import shutil
import sys

ratio = (32,32)

def resize_recursive(in_path, out_path):
    for file in os.listdir(in_path):
        if os.path.isdir(in_path+"/"+file):
            os.mkdir(out_path+"/"+file)
            resize_recursive(in_path+"/"+file, out_path+"/"+file)
        elif file[-3:] == "png":
            image = Image.open(in_path+"/"+file)
            image.thumbnail(ratio)
            image.save(out_path+"/"+file, "PNG")
        else:
            copyfile(in_path+"/"+file, out_path+"/"+file)
            
if __name__ == '__main__':
    shutil.rmtree('out', ignore_errors=True)
    os.mkdir("out")
    resize_recursive(sys.argv[1], "out")
    