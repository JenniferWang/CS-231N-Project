#!/bin/bash
PROTOTXT=4_train_test.prototxt
PREFIX=4
for i in $(ls | grep "^${PREFIX}.*caffemodel"); do
  echo $i
  ~/caffe/build/tools/caffe test -model $PROTOTXT -weights $i  2> ${PREFIX}_total_acc.log
  tail -2 ${PREFIX}_total_acc.log >> ${PREFIX}_acc
done