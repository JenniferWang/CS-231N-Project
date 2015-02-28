# In order to use caffe, we need to convert all the data into lmdb/leveldb
# format. This file generate the train.txt and val.txt for convert_data.sh
import os
import random

TRAIN_sz = 4;
VAL_sz = 1;
ROOT_DIR = "./dataset/English/Img/GoodImg/Bmp/"
NEW_DIR = "./dataset/English/Img/GoodImg/Bmp/"
TRAIN_LABEL = "train_good.txt"                      #May need to change
VAL_LABEL = "val_good.txt"                          #May need to change

counter = -1
train_f = open(NEW_DIR + TRAIN_LABEL, 'w')
val_f = open(NEW_DIR + VAL_LABEL, 'w')
img_label = []

for root, subFolders, files in os.walk(ROOT_DIR):
  if counter != -1:
    curr_root = root.split('/')[-1]
    for idx, img_file in enumerate(files):
      if img_file[-3 :] != 'png':
        continue
      img_label.append(curr_root + '/' + img_file + ' ' + str(counter) + '\n')
  counter += 1

random.shuffle(img_label)
train_num = (len(img_label) / ( TRAIN_sz + VAL_sz )) * TRAIN_sz

for idx in xrange(train_num):
  train_f.write(img_label[idx])
for idx in xrange(train_num, len(img_label)):
  val_f.write(img_label[idx])

train_f.close()
val_f.close()
