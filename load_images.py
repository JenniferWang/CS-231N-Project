import numpy as np
import os
from scipy.misc import imread

DATA_DIR = "/Users/jennifer/Box Sync/2014 - 2015/cs 231n/project/code/dataset/modified/Bmp"

def load_images_all(path, dtype=np.float32): #assume input is a colored image
  X_train = []
  y_train = []
  count = -1
  for (dirpath, dirnames, filenames) in os.walk(path):
    print filenames
    if count >= 0:
      first_file = filenames[0]
      if(first_file[0] == '.'):
        os.remove(os.path.join(dirpath, first_file))
      num_images = len(filenames)
      X_train_block = np.zeros((num_images, 3, 64, 64), dtype=dtype)
      y_train_block = count * np.ones(num_images, dtype=np.int64)
      for j, img_file in enumerate(filenames):
        img = imread(os.path.join(dirpath,img_file))
        X_train_block[j] = img.transpose(2,0,1)
      X_train.append(X_train_block)
      y_train.append(y_train_block) 
    count = count + 1
  X_train = np.concatenate(X_train, axis=0)
  y_train = np.concatenate(y_train, axis=0)
  return X_train, y_train   
  #0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2] (if we want black and white)

def load_images_partial(path, num, dtype=np.float32):
  X_train = []
  y_train = []
  count = -1
  for (dirpath, dirnames, filenames) in os.walk(path):
    if count == num:
      break
    if count >= 0:
      first_file = filenames[0]
      if(first_file[0] == '.'):
        os.remove(os.path.join(dirpath, first_file))
      num_images = len(filenames)
      X_train_block = np.zeros((num_images, 3, 64, 64), dtype=dtype)
      y_train_block = count * np.ones(num_images, dtype=np.int64)
      for j, img_file in enumerate(filenames):
        img = imread(os.path.join(dirpath,img_file))
        X_train_block[j] = img.transpose(2,0,1)
      X_train.append(X_train_block)
      y_train.append(y_train_block) 
    count = count + 1
  X_train = np.concatenate(X_train, axis=0)
  y_train = np.concatenate(y_train, axis=0)
  return X_train, y_train 


def main():

  X_train, y_train = load_images_partial(DATA_DIR, 10) #0-9
  print X_train.shape
  print y_train

if __name__ == "__main__":
    main()
