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
print feature_names
print titanic_X
