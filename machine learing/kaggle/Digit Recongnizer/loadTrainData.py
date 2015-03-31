#!/usr/bin/env python
# coding=utf-8

from numpy import *
import csv
import operator

def normal(array):
    n,m = shape(array)
    for i in xrange(n):
        for j in xrange(m):
            if array[i, j] <= 10:
                array[i, j] = 0
            else:
                array[i, j] = 1
    return array

def toInt(array):
    array = mat(array)
    m, n = shape(array)
    newarray = zeros((m, n))
    for i in xrange(m):
        for j in xrange(n):
            newarray[i, j] = int(array[i, j])
    return newarray

def loadTrainData():
    l = []
    with open('train.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l = array(l)
    label = l[:,0]
    data = l[:,1:]
    return normal(toInt(data)), toInt(label)


def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l = array(l)
    return normal(toInt(l))

def saveResult(resultList):
    with open('result.csv', 'wb') as file:
        MyWriter = csv.writer(file)
        for i in resultList:
            MyWriter.writerow(i)

def classify(inX, dataSet, labels, k):
    inX = mat(inX)
    dataSet = mat(dataSet)
    labels = mat(labels)
    dataSetSize = dataSet.shape[0]
    #print type(tile(inX, (dataSetSize, 1)))
    #print type(dataSet)
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet

    sqdiffMat = array(diffMat)**2
    sqDistances = sqdiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in xrange(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def DigitClassify():
    traindata, trainlabel = loadTrainData()
    testdata = loadTestData()
    
    m, n = shape(testdata)
    resultList = []
    for i in xrange(m):
        result = classify(testdata[i], traindata, trainlabel.transpose(), 6)
        resultList.append(result)
    saveResult(resultList)

DigitClassify()
