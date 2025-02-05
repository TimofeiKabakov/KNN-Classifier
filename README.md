# **Object Classification System with K-Nearest Neighbors**

## **Overview**

This project focuses on classifying objects from the **MPEG-7 dataset** using **K-Nearest Neighbors (KNN)**. 

By analyzing shape features through the **Histogram of Curvature Scale (HoCS)** and examining texture patterns using techniques like the **Gray-Level Co-occurrence Matrix (GLCM)** and **Local Binary Patterns (LBP)**, the model reaches a classification accuracy of up to **70%**.

The workflow includes image preprocessing, feature extraction, KNN model training, and performance evaluation through confusion matrices and classification rates.

## **Features**
* **Shape-Based Classification (HoCS)**: Extracts shape features using the Histogram of Curvature Scale method.
* **Texture-Based Classification (In progress)**: Utilizes GLCM and LBP for texture feature extraction.
* **KNN Classifier**: KNN model with fine-tuned hyperparameters.
* **Performance Metrics**: Evaluation through confusion matrices and classification rates.

## **Dataset**
**[MPEG-7 Dataset](https://dabi.temple.edu/external/shape/MPEG7/dataset.html)**: The MPEG-7 dataset includes a variety of binary images representing different object classes, with diverse shapes and textures for classification tasks.
