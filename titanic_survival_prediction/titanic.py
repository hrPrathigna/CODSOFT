# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xyMQos4zREyLK5Jw621ePzmlHedOmlzy

**Titanic Survival Prediction**
 The objective of this project is to predict whether a passenger on the titanic survived or not by using machine learning techniques.

Dataset used for this project contains information about individual passengers,such as their age,gender,ticket,class,fare,cabin etc
"""

#import modules
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#import data
titanic = pd.read_csv('tested.csv')

titanic.shape

#decsribe data
titanic.head()

titanic.info()

titanic.describe()

#Data Visualization
sns.countplot(x=titanic['Survived'],hue=titanic['Pclass'])

titanic["Sex"]

sns.countplot(x=titanic['Sex'],hue=titanic['Survived'])

#Data Preprocessing
ports = pd.get_dummies(titanic.Embarked,prefix = 'Embarked')
ports.head()

titanic = titanic.join(ports)
titanic.drop(['Embarked'],axis = 1,inplace = True)

titanic.head()

titanic.Sex = titanic.Sex.map({'male':0,'female':1})

titanic.drop(['Cabin','Ticket','Name','PassengerId'],axis = 1 ,inplace = True)

titanic.info()

titanic.isnull().values.any()

titanic[pd.isnull(titanic).any(axis = 1)]

titanic.Age.fillna(titanic.Age.mean(),inplace = True)

titanic.isnull().values.any()

titanic.Fare.fillna(titanic.Fare.mean(),inplace = True)

titanic.isnull().values.any()

#Define Target Variable (y) and Feature Variables (X)
y = titanic.Survived.copy()
X = titanic.drop(['Survived'],axis = 1)

X.info()

#Train Test Split
from sklearn.model_selection import train_test_split
X_train,X_valid,y_train,y_valid = train_test_split(X,y, test_size = 0.2, random_state = 7)

#Modeling and model evalution
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

X_train.shape, X_valid.shape, y_train.shape, y_valid.shape

model.fit(X_train,y_train)

model.intercept_

#model Prediction
model.score(X_train,y_train)

model.score(X_valid,y_valid)