*Geometric Transformsations for Medical Image Data Augmentation*
--------------------------------------
**Introdcution**
------------------------
This repository focuses on exploring different geometric transformations for medical image data augmentation. Data augmentation is crucial in training robust machine learning models, especially in the medical imaging domain. Two different approaches are employed to train the model with varying degrees of augmentation:
1. ***No Augmentation:*** The model is trained on the original, unaltered dataset.
2. ***ImageDataGenerator Augmentation:*** The keras ImageDataGenerator is utilized for augmentation, applying operations such as rotation, shear, zoom, horizontal flip, and vertical flip.
   
Then we try to inject a percentage of generated images in the training set and we evaluate the model performance

---------------------------------
**Code Structure**
---------------------------
* ***classifier.py:*** Contains the code for the classifier model.

* ***Data_augmentation:*** Contains code for generating augmented images using the keras ImageDataGenerator.

* ***data_preparation.py:*** Contains code for data preparation

* ***evalute.py:*** Contains code for model evaluation 

----------------------------- 
**Running Code**
-------------------
* To generate augmented images for the 'yes' and 'no' cases separately:         

    Run the code in python data_augment.py for ImageDataGenerator augmentation.
* To load a percentage of original and augmented_data in the training directory:

    Run the function load_data in data_preparation.py
* To evaluate the data_augmentation efficency :

    Run the code in evaluate.py
----------------------
**Results**
---------------------
We mesure in each try the test accurancy and the ROC curve area
| Number of Epochs       | 10 epochs |            | 20 epochs |            | 30 epochs |            | 40 epochs |            | 50 epochs |          |  
|------------------------|-----------|------------|-----------|------------|-----------|------------|-----------|------------|-----------|------------|
| Original Data          | 65.62%    | 0.88       | 84.38%    | 0.87       | 78.12%    | 0.88       | 71.88%    | 0.84       | 75        | 0.85       |
| 15% of Augmented Data   | 75%      | 0.84      | 65.62%      | 0.72       | 78.12%     |0.88       |56.25%      | 0.67      | 53.12%      | 0.65      | 
| 35% of Augmented Data   | 71.88%      | 0.80       | 84.38     |0.90       | 84.38      |0.90       | 75%      | 0.85       | 62.50%      |0.71      |
| 50% of Augmented Data   |  81.25%      | 0.85      | 65.62%     | 0.68       | 68.75%   | 0.80      | 56.25%     | 0.57      | 53.12      | 0.49      |
| 80% of Augmented Data   | 84.30%      | 0.90      | 75%      | 0.83       | 78.12%     | 0.82      | 78.12%      | 0.80      | 43.75%    | 0.45       | 








