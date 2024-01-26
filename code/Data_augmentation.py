import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import cv2


'''This function generates new images from the originals and saves them in a directory.
   :param dir_path: the directory path where the original images are stored
   :param save_to_dir: the directory path where you will save the generated images
   :param percentage: the percentage of original images used to generate the new ones
   :param n_sample_generated: number of samples generated from each original image 
   :return: generated images saved in the save_to_dir directory'''
def augment_data(dir_path:str,save_to_dir:str,percentage:int,n_sample_generated:int):
  data_gen=ImageDataGenerator(rotation_range=20,
                              rescale=1./255,
                              width_shift_range=.2,
                              height_shift_range=.2,
                              shear_range=0.2,
                              zoom_range=0.2,
                              horizontal_flip=True,
                              vertical_flip=True
                              fill_mode='nearest')


  files=[i for i in os.listdir(dir_path)]
  number=int(len(files)*0.01*percentage)
  i=0 #counter of random image selected
  while i<number:
        file_name=random.choice(files)
        img_path=dir_path+file_name
        img=cv2.imread(img_path)
        img=img.reshape((1,)+img.shape)
        save_prefix='aug_'+file_name
        for batch in data_gen.flow(img,batch_size=1,save_to_dir=save_to_dir,
                                   save_prefix=save_prefix, save_format='jpg'):

                  i+=1
                  if i>n_sample_generated:
                    break
  print(f'The geometric data augmentation to {dir_path} has been successfully completed.')


augment_data('TRAIN/YES/','Augmented_data/YES/',100,5)
augment_data('TRAIN/NO/','Augmented_data/NO/',100,5)