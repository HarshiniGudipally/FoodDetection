# FoodDetection
Food Detection using FRNN
Identify food items and also items in a group of food items along with bounding boxes for each food item detected in that image. 
## Getting Started 
* Used Regional Proposal Network for drawing bounding boxes.
### Prerequisites
* Download food items [Dataset](http://foodcam.mobi/dataset100.html)
* Downloaded dataset will have 100 (folders) whose corresponding label name is present in categories.txt. Inside each folder, there will be images of food item and bb_info.txt.
* Run python3 generate_bbox_files.py. This creates bounding box files for each food image..
* Run python3 create_data_file.py. This will split the food100 dataset into 2 files of images list
  accourding to the 'percentage_test'. The default is 10% will be assigned to test. 
  
  (1) train.txt - the list of training images
  (2) test.txt - the list of validating images
  
  This .txt file data will have format of image_path,b1,b2,b3,b4,category_name(Ex: /data/images/4/342.jpg,0,0,500,375,chicken-n-egg-on-rice)
* Run frcnn_train.ipynb to train a model in collab. 
* Run frcnn_test.ipynb to test a model for pridictions.
### References
[Research paper for RPN](https://arxiv.org/pdf/1506.01497.pdf)
