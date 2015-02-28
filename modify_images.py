# Recursively resize all the images
import os
from PIL import Image

ROOT_DIR = "/Users/jennifer/Box Sync/2014 - 2015/cs 231n/project/code/dataset/English/Img/GoodImg/Bmp"
NEW_DIR = "/Users/jennifer/Box Sync/2014 - 2015/cs 231n/project/code/dataset/modified/Bmp"
WIDTH = 64
HEIGHT = 64
counter = -1

for root, subFolders, files in os.walk(ROOT_DIR):
  directory = os.path.join(NEW_DIR, str(counter))
  if not os.path.exists(directory):
    os.makedirs(directory)
  for idx, img_file in enumerate(files):
    img = Image.open(os.path.join(root, img_file))
    img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS) 
    img.save(directory + '/' + str(idx) + '.png')
  counter += 1



    
