#!/usr/bin/env python
# coding=utf-8
from numpy import *
import operator
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B'];
    return group, labels

import kNN
group, labels = kNN.createDataSet()

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    
