#!/usr/bin/env sh
# Create the  lmdb inputs for image/good data
# N.B. set the path to the imagenet train + val data dirs
Label_DIR=./dataset/
ROOT_DIR=../data/English/Fnt/
python ./generate_data_labels.py $ROOT_DIR $Label_DIR train_fnt.txt val_fnt.txt

NEW_DIR=./dataset
DATA=./dataset
TOOLS=../caffe/build/tools

TRAIN_DATA_ROOT=../data/English/Fnt/
VAL_DATA_ROOT=../data/English/Fnt/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=28
  RESIZE_WIDTH=28
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in convert_data.sh to the path" \
       "where the training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in convert_data.sh to the path" \
       "where the validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --gray=true \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train_fnt.txt \
    $NEW_DIR/train_fnt_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --gray=true \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/val_fnt.txt \
    $NEW_DIR/val_fnt_lmdb

echo "Done."