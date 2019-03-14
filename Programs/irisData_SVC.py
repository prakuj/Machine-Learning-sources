import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()
X = iris.data
Y = iris.target
trainX,testX,trainY,testY=train_test_split(X,Y,test_size=0.3)
model = SVC()
model.fit(trainX,trainY)
res = model.predict(testX)
print(res)
print("accuracy = ",model.score(testX,testY))