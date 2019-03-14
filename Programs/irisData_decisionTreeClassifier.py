from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
iris = load_iris()
#print(iris)
#print (iris.feature_names)
#print (iris.target_names)
#print (iris.data.shape)
X = iris.data
Y = iris.target
trainX,testX,trainY,testY = train_test_split(X,Y,test_size=0.3)
#print (trainX.data.shape)
clf = DecisionTreeClassifier()
clf.fit(trainX,trainY)
#print(testX)
result = clf.predict(testX)
print(result)
print("Accuracy: \n", clf.score(testX, testY))