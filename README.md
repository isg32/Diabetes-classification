# Diabetes Data Prediction

This project is a practical implementation of diabetes data prediction using the K-Nearest Neighbors (KNN) algorithm. It allows users to input values for various features related to diabetes risk factors and predicts whether a person is positive or negative for diabetes based on these inputs.

## Note

Please note that the accuracy of this prediction may not be high due to the limited amount of data.

## Getting Started

To run this project locally, you will need Python installed on your system along with the required libraries. You can install the necessary dependencies using `pip`:

```bash
pip install knn
pip install streamlit
pip install matplotlib
```
Usage

# Run the application using the following command:

```bash
streamlit run app.py
```
Provide values for input features in the Streamlit interface.

Click the "Predict" button to see the prediction result.

## Input Features

The following input features can be provided:

    Pregnancies
    Glucose
    Blood Pressure
    Skin Thickness
    Insulin
    BMI (Body Mass Index)
    Diabetes Pedigree Function
    Age

## Accuracy

The K-Nearest Neighbors (KNN) algorithm has an accuracy of approximately [accuracy_percentage]% for this dataset.
Prediction Results

    If the prediction is 1, it indicates that the person is Positive for diabetes.
    If the prediction is 0, it indicates that the person is Negative for diabetes.
