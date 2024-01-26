import zipfile

zip_path='brain-tumor-detection-mri.zip'
extract_path='Brain_Tumor_dataset'

with zipfile.ZipFile(zip_path,'r') as zip_ref:
  zip_ref.extractall(extract_path)

dataset_path = 'Brain_Tumor_dataset/Brain_Tumor_Detection'