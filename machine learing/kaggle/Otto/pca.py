#!/usr/bin/env python
# coding=utf-8

import pdb
from numpy import *
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

pat = './trainafterclean.csv'
pat2 = './testafterclean.csv'
pat3 = './anssvm.csv'
pat4 = './ansNB.csv'
pat5 = './ansRF.csv'

def loadDataSet(fileName, delin = ' '):
    fr = open(fileName)
    stringArr = [line.strip().split(delin) for line in fr.readlines()]
    #pdb.set_trace();
    #print stringArr
    datArr = [map(float, line) for line in stringArr]

    fr.close()
    return mat(datArr)


def loadTrain(fileName):
    Data = loadDataSet(fileName)
    trainData = Data[:,1 :-1]
    trainTarget = Data[:, -1]
    return trainData, trainTarget
    
def pca(dataMat, topN = 9):
    meanVals = mean(dataMat, axis = 0)

    #pdb.set_trace()

    DataAdjust = dataMat - meanVals
    covMat = cov(DataAdjust, rowvar = 0)
    eigVals, eigVects = linalg.eig(mat(covMat))
    #print eigVals
    
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[: -(topN + 1): -1]
    redEigVects = eigVects[:, eigValInd]
    lowD = DataAdjust * redEigVects
    #reconMat = (lowD * redEigVects.T) + meanVals
    return lowD

def loadTestData(fileName, delin = ' '):
    fr = open(fileName)
    stringArr = [line.strip().split(delin) for line in fr.readlines()]
    datArr = [map(float, line) for line in stringArr]
    datArr = mat(datArr)
    datArr = datArr[:,1:]
    fr.close()
    return mat(datArr)


def main():
    trainData , trainTarget = loadTrain(pat)
    trainData = pca(trainData)

    #classfication
    #clf = svm.SVC()
    #clf = GaussianNB()
    clf = RandomForestClassifier(n_estimators = 10)
    clf = clf.fit(trainData, ravel(trainTarget))

    testData = loadTestData(pat2)
    testData = pca(testData)

    ans = clf.predict(testData) 

    fw = open(pat5, 'a')

    for l in ans:
        l = str(l)
        fw.write(l)
        fw.write('\n')

    fw.close()


main()


