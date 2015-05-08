#!/usr/bin/env python
# coding=utf-8

import csv
import pandas as pd
import numpy as np
from scipy.optimize import minimize
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss

import os

pth = ['1.csv', '2.csv', '3.csv']

os.system("ls ../ans3.0/")

train = pd.read_csv("../ans3.0/train.csv")
print ("Training set has {0[0]} rows and {0[1]} columns".format(train.shape))

labels = train['target']
train.drop(['target', 'id'], axis = 1, inplace = True)

sss = StratifiedShuffleSplit(labels, test_size = 0.05, random_state = 1234)


for train_index, test_index in sss:
    train_x, train_y = train.values[train_index], labels.values[train_index]
    test_x, test_y = train.values[test_index], labels.values[test_index]
    break


clfs = []
rfc = RandomForestClassifier(n_estimators = 50, random_state = 3333, n_jobs = -1)
rfc.fit(train_x, train_y)
print ('RFC logLoss {score}'.format(score = log_loss(test_y, rfc.predict_proba(test_x))))
clfs.append(rfc)


logreg = LogisticRegression()
logreg.fit(train_x, train_y)
print ('logistic logLoss {score}'.format(score = log_loss(test_y, logreg.predict_proba(test_x))))
clfs.append(logreg)


rfc2 = RandomForestClassifier(n_estimators = 50, random_state = 4141, n_jobs = -1)
rfc2.fit(train_x, train_y)
print ('RFC2 logLoss {score}'.format(score = log_loss(test_y, rfc2.predict_proba(test_x))))
clfs.append(rfc2)

def saveResult(x, i):
    with open(pth[i], 'wb') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(["id","Class_1", "Class_2","Class_3","Class_4","Class_5","Class_6","Class_7","Class_8","Class_9"])
        id_num = 1
        for eachlabel in x:
            l = []
            l.append(id_num)
            l.extend(eachlabel)
            myWriter.writerow(l)
            id_num += 1


con = 0
for clf in clfs:
    test = pd.read_csv('./test.csv')
    test.drop(['id'], axis = 1, inplace = True)
    lab = clf.predict_proba(test)
    saveResult(lab, con)
    con += 1


"""
predictions = []

for clf in clfs:
    predictions.append(clf.predict_proba(test_x))


def log_loss_func(weights):
    final_prediction = 0
    for weight , prediction in zip(weights, predictions):
        final_prediction += weight * prediction

    return log_loss(test_y, final_prediction)


starting_values = [0.5] * len(predictions)

cons = ({'type':'eq', 'fun':lambda w : 1 - sum(w)})

bounds = [(0, 1)] * len(predictions)

res = minimize(log_loss_func, starting_values, method = 'SLSQP', bounds = bounds, constraints = cons)

print ('Ensamble Score : {best_score}'.format(best_score = res['fun']))
print ('Best Weights: {weights}'.format(weights = res['x']))
"""
