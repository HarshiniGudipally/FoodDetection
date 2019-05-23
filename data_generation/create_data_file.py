# food100_split_for_yolo.py
#
# This script will split the food100 dataset into 2 files of images list
# accourding to the 'percentage_test'. The default is 10% will be assigned to test.
# (1) train.txt - the list of training images
# (2) test.txt - the list of validating images
#
# Credit: script is originated from blob post description
# <https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/>
#
import glob, os

import cv2
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/home/techolution/work/project/frcnn/data_generation/data/images/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train_d.txt', 'w')
file_test = open('test_d.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
# for pathAndFilename in glob.iglob(os.path.join(current_dir, "images/*/*.jpg")):
#     title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#
#     if counter == index_test:
#         counter = 1
#         #file_test.write(path_data + title + '.jpg' + "\n")
#         file_test.write(pathAndFilename + "\n")
#     else:
#         #file_train.write(path_data + title + '.jpg' + "\n")
#         file_train.write(pathAndFilename + "\n")
#         counter = counter + 1

for root,folders,files in os.walk(path_data):
    for folder in folders:
        category_name = str(folder)
        for _,__,image_files in os.walk(os.path.join(path_data, folder)):
            for file in image_files:
                if file.endswith(".jpg"):
                    file_name = str(file)
                    image_path = os.path.join(os.path.join(path_data,folder),
                                       file_name)

                    # print(image_path)
                    img = cv2.imread(image_path)

                    txt_file = file_name.split(".")
                    boundingb_path = os.path.join(os.path.join(path_data,folder),
                                      txt_file[0]\
                                     + \
                                     ".txt")
                    file = open(boundingb_path,'r')
                    file_read= file.readlines()
                    boundingb_data = file_read[1].strip()
                    boundingb_data = boundingb_data.split(" ")
                    file.close()

                    final_data = image_path + "," + boundingb_data[0] + "," + boundingb_data[1] + "," + boundingb_data[2] + "," + boundingb_data[3] + "," + boundingb_data[4]
                    # print((final_data))
                    if counter == index_test:
                        counter = 1
                        train_path \
                            ="/home/techolution/work/project/frcnn/data_generation/test/" + str(folder) + str("/") + file_name
                        print(train_path
                              )
                        cv2.imwrite(train_path, img)
                        file_test.write(final_data + "\n")
                    else:
                        test_path = \
                            "/home/techolution/work/project/frcnn/data_generation/train/" + str(folder) + str("/") + file_name
                        print(test_path)
                        cv2.imwrite(test_path, img)
                        file_train.write(final_data + "\n")
                        counter = counter + 1




