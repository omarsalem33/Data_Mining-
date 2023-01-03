import pandas as pd
from sklearn.model_selection import train_test_split
import math
Data_set = pd.read_csv("IRIS.csv", delimiter=",")
Features_names= Data_set.columns[0:4]
print(Features_names)
target=Data_set['species'].tolist()


target= list(set(target))
print(target)
X = Data_set[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
print(X)
y = Data_set["species"]
print(y)

# Data Preprocessing

from sklearn import preprocessing
import numpy as np

label_gender = preprocessing.LabelEncoder()
print(Data_set.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=3)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn import metrics
from sklearn.metrics import confusion_matrix

################KNN###################

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=12)
neigh.fit(X_train, y_train)
predicted = neigh.predict(X_test)
print("\nPredicted by KNN",predicted)
results=confusion_matrix(y_test, predicted)
print("\n KNN confusion matrix",results)
print("\nKNN Accuracy: ", metrics.accuracy_score(y_test, predicted))


#################Naive#################

from sklearn.naive_bayes import GaussianNB

model=GaussianNB()

model.fit(X_train, y_train)
predicted=model.predict(X_test)
print("\nPredicted by Naive",predicted)
results=confusion_matrix(y_test, predicted)
print("\n Naive confusion matrix",results)
print("\nNaive  Accuracy: ", metrics.accuracy_score(y_test, predicted))