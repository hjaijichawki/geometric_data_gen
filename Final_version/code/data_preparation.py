import os
import shutil




def split_data(dataset_path:str):
    '''This function is used to split dataset into train/test/val in directories TRAIN, TEST and VAL already created in a tree structure
       :param dataset_path: the path of the dataset intended to split it
       :return: dataset splitted into train/test/val and saved in the directories TRAIN, TEST and VAL''' 
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



def load_data(dataset_path:str,TRAIN_path:str,percentage:int):

  '''This function is used to load a percentage of data from a directory and it in another one
     :param dataset_path: the directory path where your data is saved
     :param TRAIN_path: the directory path where you will save the percentage of loaded data and train the model on it
     :param percentage: the percentage of data you want to load it
     :return: the percentage desired of data is saved into the TRAIN_path '''
  
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
