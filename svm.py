# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:50:41 2020

@author: Matthew Gerring
"""

import numpy as np
from sklearn import preprocessing, model_selection, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.drop(['id'], 1, inplace=True)
df.replace('?',-99999, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(C=5)


clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print("Confidence = ", confidence)

example_measures = np.array([[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print("prediction = ", prediction)