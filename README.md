*Geometric Transformations for Medical Image Data Augmentation*
--------------------------------------

**Introduction**
------------------------
In the realm of ML, the efficacy of models is related to the quantity and quality of the data used for their training, the more diverse and plentiful the data, the better the models generalize. However, in many cases, there is a scarcity of diverse and comprehensive datasets required for effective model training. In this context, data augmentation emerges as a crucial measure to mitigate the impact of data scarcity by artificially increasing the volume of training data through the application of techniques which generate new data.
This repository focuses on exploring different geometric transformations applied to generate new medical images such as rotation, shear, zoom, horizontal flip, and vertical flip. Two different approaches are employed to train the model with varying the training dataset:
1. ***Without Data Augmentation:*** The model is trained on the original, unaltered dataset.
2. ***With Data Augmentation:*** The model is trained on the dataset with new generated images.
   
Then we try to inject a percentage of generated images in the training dataset and we evaluate the model performance


**Dataset**
----------------

You find here the link for the dataset.
[Brain Tumor Detection MRI Dataset](https://www.kaggle.com/datasets/abhranta/brain-tumor-detection-mri?fbclid=IwAR0vZxyXazz_k64eRmOP7X-ltavMYQl5dS28QSskOXV2mEnMdEXjfhLiCPA)


**Code Structure**
---------------------------

* ***classifier.py:*** Contains the code for the classification model.

* ***Data_augmentation.py:*** Contains the code for generating new images from originals.

* ***data_preparation.py:*** Contains the code for data preparation.

* ***evalute.py:*** Contains the code for model evaluation. 
  


**Running Code**
-------------------

* Download the dataset by following the instructions below:

    download kaggle's beta API

    Execute the following commands
    ```
        install kaggle.json 
        !pip install -q kaggle
        !mkdir ~/.kaggle
        !cp kaggle.json ~/.kaggle/
        !chmod 600 ~/.kaggle/kaggle.json
        !kaggle datasets download -d abhranta/brain-tumor-detection-mri
  
* Prepare the tree project structure:

  Execute the following commands
    ``` 
        !apt-get install tree
        !mkdir TRAIN TRAIN_model TEST VAL 
        !mkdir Brain_Tumor_data Augmented_data
        !mkdir TRAIN/YES TRAIN/NO TEST/YES TEST/NO
        !mkdir VAL/YES VAL/NO
        !mkdir  Augmented_data/YES Augmented_data/NO
        !tree -d 

* Execute the command `pip install -r requirements.txt`
* Run the code `dataset_extract.py` to extract the dataset from a zip file
* Use the function `split_data` in `data_preparation.py` to split dataset into train/test/val
  
* Run the code in `classifier.py` to classify original data

* Run the code in `Data_augmentation.py` to generate new images
  
* Load x% of original data and 100-x% of new generated data in the TRAIN_model directory
  
* Change the TRAIN_DIR to TRAIN_model and run the classifier to test the impact of using new generated data

* Evaluate the model performance each time with the code in `evaluate.py`

**Results**
---------------------

We measure the test accuracy and the area under the ROC curve in each attempt

| Number of Epochs       | 10 epochs |            | 20 epochs |            | 30 epochs |            | 40 epochs |            | 50 epochs |          |  
|------------------------|-----------|------------|-----------|------------|-----------|------------|-----------|------------|-----------|------------|
| Original Data          | 65.62%    | 0.88       | 84.38%    | 0.87       | 78.12%    | 0.88       | 71.88%    | 0.84       | 75%        | 0.85       |
| 15% of Augmented Data   | 75%      | 0.84      | 65.62%      | 0.72       | 78.12%     |0.88       |56.25%      | 0.67      | 53.12%      | 0.65      | 
| 35% of Augmented Data   | 71.88%      | 0.80       | 84.38%    |0.90       | 84.38%      |0.90       | 75%      | 0.85       | 62.50%      |0.71      |
| 50% of Augmented Data   |  81.25%      | 0.85      | 65.62%     | 0.68       | 68.75%   | 0.80      | 56.25%     | 0.57      | 53.12%     | 0.49      |
| 80% of Augmented Data   | 84.30%      | 0.90      | 75%      | 0.83       | 78.12%     | 0.82      | 78.12%      | 0.80      | 43.75%    | 0.45       | 

**Contribution**
------------------------

Contributions are welcome! Feel free to open issues or create pull requests to enhance the functionality or address any improvements.






