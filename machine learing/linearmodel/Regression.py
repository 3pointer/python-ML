#!/usr/bin/env python
# coding=utf-8

from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
boston = load_boston()

# print boston.data.shape
# print boston.feature_names
x = np.max(boston.data)

n, m = boston.data.shape
"""
for i in xrange(1,n):
    for j in xrange(1,m):
        print boston.data[i][j]
        #if boston.data[i][j] == x:
        #    print i,j,
    print
"""


# x = np.array([[1,-10],[3,30],[4,12]])   n*m矩阵的mean test
# print np.mean(x)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    boston.data, boston.target, test_size=0.25, random_state=3)

from sklearn.feature_selection import *
fs = SelectKBest(score_func=f_regression, k=5)
X_new = fs.fit_transform(X_train, y_train)
print zip(fs.get_support(), boston.feature_names)

x_min, x_max = X_new[:,0].min() - .5, X_new[:,0].max() + .5 #normalization!!!! feature2 is not avaiable to see
y_min, y_max = y_train.min() - .5, y_train.max() +.5

"""
fig, axes = plt.subplots(1, 5)
fig.set_size_inches(10, 10)

for i in range(5):
    #axes[i].set_aspect('equal')
    axes[i].set_title('feature' + str(i))
    axes[i].set_xlabel('feature')
    axes[i].set_ylabel('Median house value')
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(y_min, y_max)
    plt.sca(axes[i])
    plt.scatter(X_new[:, i], y_train)
plt.show()
"""


from sklearn.preprocessing import StandardScaler
scalerX = StandardScaler().fit(X_train)
scalery = StandardScaler().fit(y_train)

X_train = scalerX.transform(X_train)
X_test= scalerX.transform(X_test)
y_train = scalery.transform(y_train)
y_test = scalery.transform(y_test)

X_new = fs.fit_transform(X_train, y_train)

x_min, x_max = X_new[:,0].min() - .5, X_new[:,0].max() + .5
y_min, y_max = y_train.min() - .5, y_train.max() +.5

fig, axes = plt.subplots(1, 5)
fig.set_size_inches(10, 10)

for i in range(5):
    #axes[i].set_aspect('equal')
    axes[i].set_title('feature' + str(i))
    axes[i].set_xlabel('feature')
    axes[i].set_ylabel('Median house value')
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(y_min, y_max)
    plt.sca(axes[i])
    plt.scatter(X_new[:, i], y_train)
plt.show()

