#plot acc / loss
import os
import sys
import matplotlib.pyplot as plt

argv = sys.argv
file_path = argv[1]

acc = []
loss = []

with open(file_path, 'r') as f:
  while True:
    line1 = f.readline()
    line2 = f.readline()
    if not line1: 
      break;
    acc.append(line1.split('=')[1])
    loss.append(line2.split('=')[1])


acc_figure = plt.figure()
loss_figure = 
plt.plot(acc)
plt.ylabel("accuracy on test set")
plt.show()

plt.figure
