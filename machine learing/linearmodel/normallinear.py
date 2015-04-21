#!/usr/bin/env python
# coding=utf-8

from sklearn.linear_model import LinearRegression
import numpy as np

np.random.seed(0)
size = 5000

X = np.random.normal(0, 1, (size, 3))
#Y = X0 + 2 * X1 + noise
Y = X[:, 0] + 2 * X[:, 1] + np.random.normal(0, 2, size)
lr = LinearRegression()
lr.fit(X, Y)

def pretty_print_linear(coefs, names = None, sort = False):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    if sort:
        lst = sorted(lst, key = lambda x : -np.abs(X[0]))
    return ''+''.join("%s * %s " % (round(coef, 5), name)for coef, name in lst)

print "linear Model:", pretty_print_linear(lr.coef_)
