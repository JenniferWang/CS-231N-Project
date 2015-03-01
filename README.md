# Google Street View Character Recognition
### CS 231N class project

##Dataset:

 * [The Chars74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)
 * Use ```./dataset/get_dataset.sh ``` to download the whole dataset
 * There are three kinds of data : 
 	* EnglishImg: Streetview Image
 	* EnglishHnd: Hand-drawn characters, 55 samples per class 
 	* EnglishFnt: Synthetic characters from computer fonts with 4 variations


##Strategy:
 * We first train an multi-class SVM on the EnglishImg data to identify numbers and use it as a bench mark.
 	* We train SVM to classify numbers, and only use good images for training
 	* We first convert the images to grayscale and use HOG as featur		
 	* SVM can achieve an accuracy of 0.76 on validation set 	
 * We then use transfer learning (fine tuning) to train a CNN and we expect it to achieve higher accuracy than SVM
	* We first train LeNet on MNIST data set following this [tutorial](http://caffe.berkeleyvision.org/gathered/examples/mnist.html)
    * We then fine tune the trained model to classify street view characters

##Working on Caffe:
 * Prepare dataset
 	* Caffe needs data in lmdb/leveldb format. In order to convert the data set
 		first run run```./code_ for_caffe/create_img_good.sh```. 
 	* There are three different kind of data. In order to gain different combination of training data and validation data, you need to change ```create_data.sh```.
    
 * 
 

