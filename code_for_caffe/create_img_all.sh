#!/usr/bin/env sh
file1="./dataset/train_fnt.txt"
if [ -f "$file1" ]
then
  echo "$file1 found."
else
  echo "$file1 not found. Run create_img_fnt.sh first"
  bash ./create_img_fnt.sh
fi

file2="./dataset/train_good.txt"
if [ -f "$file2" ]
then
  echo "$file2 found."
else
  echo "$file2 not found. Run create_img_good.sh first"
  bash ./create_img_good.sh
fi

file3="./dataset/train_all.txt"
cat $file1 $file2 > $file3

file4="./dataset/val_fnt.txt"
file5="./dataset/val_good.txt"
file6="./dataset/val_all.txt"
cat $file4 $file5 > $file6