import os
import shutil
import zipfile

zip_path='brain-tumor-detection-mri.zip'
extract_path='Brain_Tumor_dataset'

with zipfile.ZipFile(zip_path,'r') as zip_ref:
  zip_ref.extractall(extract_path)

dataset_path = 'Brain_Tumor_dataset/Brain_Tumor_Detection'

#Splitting data into TRAIN/TEST/VAL
def split_data(dataset_path):
    ignored={"pred"}
    directories=[i for i in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path,i)) if not i in ignored]
    for CLASS in directories:
        if CLASS not in ignored:
            if not CLASS.startswith('.'):
                IMG_NUM=len(os.listdir(dataset_path+'/'+CLASS))
                n_train=int(0.8*IMG_NUM)
                n_val=int(0.9*IMG_NUM)
                for (n,FILE_NAME) in enumerate(os.listdir(dataset_path+'/'+CLASS)):
                    img=dataset_path+'/{}/{}'.format(CLASS,FILE_NAME)
                    if n<n_train:
                        shutil.copy(img,'TRAIN/{}/{}'.format(CLASS.upper(),FILE_NAME))
                    elif n in range(n_train,n_val):
                        shutil.copy(img,'TEST/{}/{}'.format(CLASS.upper(),FILE_NAME))
                    else:
                        shutil.copy(img,'VAL/{}/{}'.format(CLASS.upper(),FILE_NAME))


#loading data from a dataset_path to a TRAIN_path with a rate equal to percentage
def load_data(dataset_path,TRAIN_path,percentage):
  ignored={"pred"}
  directories=[i for i in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path,i)) and i not in ignored]
  number_files=0
  for subdir in directories:
    path=dataset_path+'/'+subdir
    number_files+=len(os.listdir(path))
  number=int(number_files*0.01*percentage)
  for CLASS in directories:
   if not CLASS.startswith('.'):
     IMG_NUM=len(os.listdir(dataset_path+'/'+CLASS))
     for (n,FILE_NAME) in enumerate(os.listdir(dataset_path+'/'+CLASS)):
      img=dataset_path+'/{}/{}'.format(CLASS,FILE_NAME)
      if n<number:
        shutil.copy(img,'{}/{}/{}'.format(TRAIN_path,CLASS.upper(),FILE_NAME))
