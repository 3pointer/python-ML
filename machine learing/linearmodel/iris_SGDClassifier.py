#!/usr/bin/env python
# coding=utf-8

import sklearn as sk
import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()
X_iris, Y_iris = iris.data, iris.target


from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

X, Y = X_iris[:, :2], Y_iris
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 33)

scaler = StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

color = ['red', 'greenyellow', 'blue']
for i in xrange(len(color)):
    px = X_train[:, 0][Y_train == i]
    py = X_train[:, 1][Y_train == i]
    plt.scatter(px, py, c = color[i])


plt.legend(iris.target_names)
plt.xlabel('length')
plt.ylabel('width')


from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, Y_train)

x_min, x_max = X_train[:,0].min() - .5, X_train[:,0].max() + .5
y_min, y_max = X_train[:,1].min() - .5, X_train[:,1].max() + .5
xs = np.arange(x_min, x_max, 0.5)
fig, axes = plt.subplots(1, 3)

fig.set_size_inches(10, 6)
for i in xrange(len(clf.intercept_)):
    axes[i].set_aspect('equal')
    axes[i].set_title('Class' + str(i) + 'versus the rest')
    axes[i].set_xlabel('length')
    axes[i].set_ylabel('width')
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(y_min, y_max)
    plt.sca(axes[i])
    for j in xrange(len(color)):
        px = X_train[:,0][Y_train == j]
        py = X_train[:,1][Y_train == j]
        plt.scatter(px, py, c = color[j])
    ys = (i - clf.intercept_[i] - xs * clf.coef_[i, 0])/clf.coef_[i, 1]
    plt.plot(xs, ys, hold = True)
#plt.show()

from sklearn import metrics
Y_train_pred = clf.predict(X_train)
print metrics.accuracy_score(Y_train, Y_train_pred)
Y_pred = clf.predict(X_test)
print metrics.accuracy_score(Y_test, Y_pred)

print metrics.classification_report(Y_test, Y_pred, target_names = iris.target_names)


from sklearn.cross_validation import cross_val_score, KFold
from sklearn.pipeline import Pipeline

clf = Pipeline([
    ('scaler', StandardScaler()),
    ('linear_model', SGDClassifier())
])

cv = KFold(X.shape[0], 6, shuffle = True, random_state = 33)
scores = cross_val_score(clf, X, Y, cv = cv)
print scores


from scipy.stats import sem

def mean_score(scores):
    return ("Mean score: {0:.3f} (+/-{1:.3f})").format(np.mean(scores), sem(scores))


print mean_score(scores)
