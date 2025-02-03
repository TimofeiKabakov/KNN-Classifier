# **Object Classification with K-Nearest Neighbors (KNN)**

## **Overview**

This project focuses on classifying objects from the **MPEG-7 dataset** using **K-Nearest Neighbors (KNN)**. 

By extracting shape descriptors such as the Histogram of Curvature Scale (HoCS) and leveraging texture analysis techniques like Gray-Level Co-occurrence Matrix (GLCM) and Local Binary Patterns (LBP), the model achieves a classification accuracy of up to **70%**. 

The workflow includes image preprocessing, feature extraction, KNN model training, and performance evaluation through confusion matrices and classification rates.

## **Features**
* **Shape-Based Classification (HoCS)**: Extracts shape features using the Histogram of Curvature Scale method.
* **Texture-Based Classification (In progress)**: Utilizes GLCM and LBP for robust texture feature extraction.
* **KNN Classifier**: KNN model with fine-tuned hyperparameters for high classification performance.
* **Performance Metrics**: Evaluation through confusion matrices and classification rates.

## **Dataset**
**[MPEG-7 Dataset](https://dabi.temple.edu/external/shape/MPEG7/dataset.html)**: The MPEG-7 dataset includes a variety of binary images representing different object classes, with diverse shapes and textures for classification tasks.
