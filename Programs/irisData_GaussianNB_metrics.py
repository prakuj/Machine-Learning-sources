import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


iris = load_iris()
X = iris.data
Y = iris.target
trainX,testX,trainY,testY=train_test_split(X,Y,test_size=0.3)
model = GaussianNB()
model.fit(trainX,trainY)
expected = testY
predicted = model.predict(testX)

# summarize the fit of the model
print(predicted)
print("accuracy = ",model.score(testX,testY))
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))