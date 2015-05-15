#!/usr/bin/env python
# coding=utf-8

from numpy import *
import matplotlib.pyplot as plt
from random import *

def loadData():
    x = arange(-1, 1, 0.02)
    y = ((x * x - 1) ** 3 + 1) * (cos(x * 2) + 0.6 * sin(x * 1.3))
    xr =[]; yr = []; i = 0
    for xx in x:
        yy = y[i]
        d = float(randint(80, 120)) / 100
        i += 1
        xr.append(xx * d)
        yr.append(yy * d)
    return x, y, xr, yr
def XY(x, y, order):
    X = []
    for i in range(order + 1):
        X.append(x ** i)
    X=mat(X).T
    Y=array(y).reshape((len(y), 1))
    return X, Y

def figPlot(x1, y1, x2, y2):
    plt.plot(x1, y1, color = 'g', linestyle = '-', marker = '')
    plt.plot(x2, y2, color = 'm', linestyle = '', marker = '.')
    plt.show();

def Main():
    x, y, xr, yr = loadData()
    X, Y = XY(array(xr), array(yr), 9) #都比，x, y 是正经答案，xr， yr是测试数据
    #X, Y = XY(x, y, 9);
    XT = X.transpose()
    B = dot(dot(linalg.inv(dot(XT,X)), XT), Y)
    myY = dot(X, B)
    figPlot(x, myY, xr, yr)
    #figPlot(x, y, xr, yr)
Main()
