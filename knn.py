import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("data/diabetes.csv")

encoder = LabelEncoder()
data["Outcome"] = encoder.fit_transform(data["Outcome"])
# print(data.shape)
# print(data.head(10))
# print(pd.DataFrame(data))
# data.describe(include="all")
# print(data.isnull().sum())

plot = plt.scatter(data["Glucose"], data["Outcome"], label="stars", color="blue", marker="*", s=30)
print(data.head(10))

x = data.drop(["Outcome"], axis=1)
y = data.drop(["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

x_train = x_train.values
y_train = y_train.values

knn_do = KNeighborsClassifier(n_neighbors=15)
knn_do.fit(x_train, y_train)

pred = knn_do.predict(x_test)
askore = accuracy_score(pred, y_test)

print(f"Our prediction is {pred} \nThe accuracy is {askore.__round__(2) * 100}%")
