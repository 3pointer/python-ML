#!/usr/bin/env python
# coding=utf-8


path = '../../../kaggle/t.csv'

import csv
import numpy as np

with open(path, 'rb') as csvfile:
    titanic_reader = csv.reader(csvfile, delimiter=',',quotechar='"')

    row = titanic_reader.next()
    feature_names = np.array(row)

    titanic_X = []
    titanic_y = []
    for row in titanic_reader:
        titanic_X.append(row)
        titanic_y.append(row[2])
    titanic_X = np.array(titanic_X)
    titanic_y = np.array(titanic_y)

#print feature_names,titanic_X[0], titanic_y[0]
titanic_X = titanic_X[:, [1, 4, 10]]
feature_names = feature_names[[1, 4, 10]]
#print feature_names
#print titanic_X
ages = titanic_X[:, 1]
mean_age = np.mean(titanic_X[ages != 'NA', 1].astype(np.float))
titanic_X[ages == 'NA', 1] = mean_age

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
label_encoder = enc.fit(titanic_X[:,2])

integer_classes = label_encoder.transform(label_encoder.classes_)

titanic_X[:, 2] = label_encoder.transform(titanic_X[:, 2])

from sklearn.preprocessing import OneHotEncoder
enc = LabelEncoder()
label_encoder = enc.fit(titanic_X[:,0])
integer_classes = label_encoder.transform(label_encoder.classes_).reshape(3, 1)

enc = OneHotEncoder()
one_hot_encoder = enc.fit(integer_classes)
new_feature = one_hot_encoder.transform(label_encoder.transform(titanic_X[:, 0]).reshape(titanic_X[:,0].shape[0], 1))
titanic_X = np.concatenate([titanic_X, new_feature.toarray()], axis = 1)

titanic_X = np.delete(titanic_X, [0], 1)
feature_names = ['age', 'sex', 'first_class', 'second_class', 'third_class']
titanic_X = titanic_X.astype(float)
titanic_y = titanic_y.astype(float)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(titanic_X, titanic_y, test_size = 0.25, random_state = 33)

