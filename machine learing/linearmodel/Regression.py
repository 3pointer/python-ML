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
    boston.data, boston.target, test_size=0.25, random_state=33)

from sklearn.feature_selection import *
fs = SelectKBest(score_func=f_regression, k=5)
X_new = fs.fit_transform(X_train, y_train)
print zip(fs.get_support(), boston.feature_names)

x_min, x_max = X_new[:,0].min() - .5, X_new[:,0].max() + .5 #normalization!!!! feature2 is not avaiable to see
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


from sklearn.preprocessing import StandardScaler
scalerX = StandardScaler().fit(X_train)
scalery = StandardScaler().fit(y_train)

X_train = scalerX.transform(X_train)
X_test= scalerX.transform(X_test)
y_train = scalery.transform(y_train)
y_test = scalery.transform(y_test)
#print np.max(X_train), np.min(X_train), np.mean(X_train), np.max(y_train), np.min(y_train), np.mean(y_train)

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




from sklearn.cross_validation import *
def train_and_evaluate(clf, X_train, y_train):
    clf.fit(X_train, y_train)
    print "Coeffcient of determination on training set:", clf.score(X_train, y_train)
    cv = KFold(X_train.shape[0], 5, shuffle=True, random_state=33)
    scores = cross_val_score(clf, X_train, y_train, cv = cv)
    print "Average coefficient of determination using 5-fold crosscalidation:", np.mean(scores)

from sklearn import linear_model
clf_sgd = linear_model.SGDRegressor(loss='squared_loss', penalty=None, random_state = 33)
train_and_evaluate(clf_sgd, X_train, y_train)
#print clf_sgd.coef_

clf_sgd1 = linear_model.SGDRegressor(loss='squared_loss', penalty='l1', random_state = 33)
train_and_evaluate(clf_sgd1, X_train, y_train)
#print clf_sgd1.coef_

clf_sgd2 = linear_model.SGDRegressor(loss='squared_loss', penalty='l2', random_state = 42)
train_and_evaluate(clf_sgd2, X_train, y_train)
#print clf_sgd2.coef_

from sklearn import svm
clf_scm = svm.SVR(kernel = 'linear')
train_and_evaluate(clf_scm, X_train, y_train)
#print clf_scm.coef_

clf_svr_poly= svm.SVR(kernel='poly')
train_and_evaluate(clf_svr_poly,X_train,y_train)

clf_svr_rbf= svm.SVR(kernel='rbf')
train_and_evaluate(clf_svr_rbf,X_train,y_train)

clf_svr_poly2= svm.SVR(kernel='poly',degree=2)
train_and_evaluate(clf_svr_poly2,X_train,y_train)

from sklearn import ensemble
clf_et = ensemble.ExtraTreesRegressor(n_estimators=10, random_state=42)
train_and_evaluate(clf_et, X_train, y_train)

print np.sort(zip(clf_et.feature_importances_,boston.feature_names),axis=0)

from sklearn import metrics

def measure_performance(X, y, clf, show_accuracy=True,show_classification_report=True,show_confusion_matrix=True,show_r2_score=False):
    y_pred = clf.predict(X_test)
    if show_accuracy:
        print "Accuracy:{0:.3f}".format(metrics.accuracy_score(y, y_pred)),"\n"

    if show_classification_report:
        print "Classification report"
        print metrics.classification_report(y, y_pred),"\n"

    if show_confusion_matrix:
        print "confusion matrix"
        print metrics.confusion_matrix(y, y_pred),"\n"

    if show_r2_score:
        print "coefficient of determination:{0:.3f}".format(metrics.r2_score(y, y_pred)),"\n"
