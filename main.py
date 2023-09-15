import knn
from knn import *
import streamlit as sl
import matplotlib.pyplot as plt

sl.title("Practical: DIABITIES DATA PRIDICTION")

sl.write("> Note: the accuracy may not be hight due to Very tiny data.")

colvals = {}

defaultvals = {
    "Pregnancies":10, "Glucose":190, "BloodPressure":88, "SkinThickness":40, "Insulin":2, "BMI":22.9, "DiabetesPedigreeFunction":0.789, "Age":80
}
colmns = {
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
}

with sl.expander("Provide values for input features"):
    for i in colmns:
        value = sl.number_input(f"Enter {i}:", key=i)
        colvals[i] = value

sl.write(f"### K-Nearest Neighbors has an accuracy of   {askore.__round__(2) * 100} %")
if colvals["Pregnancies"] == 0:
    input_values = [defaultvals[i] for i in colmns]
else:
    input_values = [colvals[i] for i in colmns]

prediction = knn.pred[8]

fictdic = []
for i in knn.pred:
    if i == 1:
        fictdic.append("yes")
    else:
        fictdic.append("no")

if sl.button("Predict"):
    if prediction == 1:
        sl.write("Positive For Diabities")
    else:
        sl.write("Negetive For Diabities")


sl.write("""
---
### Completed algorithms:

- [x] KNN
- [ ] SVM
- [ ] logistic regression
- [ ] Random Forest 
---
""")
sl.write(f"""
| Method | Accuracy |
| ----------- | ----------- |
| KNN | {askore.__round__(2) * 100}% |
""")
