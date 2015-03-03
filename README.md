# Google Street View Character Recognition
### CS 231N class project

##Dataset:

 * We use [The Chars74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)
 * There are three kinds of data : 
 	* EnglishImg: Streetview Image
 	* EnglishHnd: Hand-drawn characters, 55 samples per class 
 	* EnglishFnt: Synthetic characters from computer fonts with 4 variations
 * We do not use EnglishHnd data in this project. And there are two kinds of data in EnglishImg: good and bad. We first consider only the good images.


##Strategy:
 * We first train a multi-class SVM on the EnglishImg data to identify numbers and use it as a bench mark.
 	* We train SVM to classify numbers, and only use good images for training
 	* We first convert the images to grayscale and use HOG as featur		
 	* SVM can achieve an accuracy of 0.76 on validation set 	
 * We then use transfer learning (fine tuning) to train a CNN and we expect it to achieve higher accuracy than SVM
	* We first train LeNet on MNIST data set following this [tutorial](http://caffe.berkeleyvision.org/gathered/examples/mnist.html)
    * We then fine tune the trained model to classify street view characters. Fine tuning tutorials can be found [here](http://caffe.berkeleyvision.org/gathered/examples/finetune_flickr_style.html)

##Working on Caffe:
 * All the codes related to caffe are in ```./code_for_caffe```
 * Prepare dataset
 	* First run ```initial.sh```
 	* run ```../data/get_dataset.sh``` to download the data
 	* Caffe needs data in lmdb/leveldb format. In order to convert the data, 
 		run```create_img_good.sh``` and ```create_img_fnt.sh``` respectively.
 	* We have already trained MNIST on caffe and store the model in ```./models```. The prototxts for the fine tuning model are also stored in this folder.
 	* Run ```./models/char74_train_sh``` to train and test the new model.
    

