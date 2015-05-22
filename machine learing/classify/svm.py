#!/usr/bin/env python
# coding=utf-8


from sklearn.datasets import fetch_olivetti_faces
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

faces = fetch_olivetti_faces()

def print_faces(images, target, top_n):
    fig = plt.figure(figsize=(18, 18))
    fig.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1, hspace = 0.05, wspace = 0.05)
    
    for i in range(top_n):
        p = fig.add_subplot(20, 20, i + 1, xticks = [], yticks = [])
        p.imshow(images[i], cmap=plt.cm.bone)

        p.text(0, 20, str(target[i]))
        p.text(0, 60, str(i))
    plt.show()

print_faces(faces.images, faces.target, 200)
plt.show()


from sklearn.svm import SVC
clf = SVC(kernel='linear')


from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(faces.data, faces.target, test_size = 0.25, random_state = 33)


from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem

def evaluate_cross_validation(clf, X, Y, K):
    cv = KFold(len(Y), K, shuffle=True, random_state = 0)
    scores = cross_val_score(clf, X, Y, cv=cv)
    print scores
    print ("MEAN score: {0:.3f}(+/-{1:.3f})").format(np.mean(scores), sem(scores))


#evaluate_cross_validation(clf, X_train, Y_train, 5)

from sklearn import metrics

def train_and_evaluate(clf, X_train, X_test, Y_train, Y_test):
    clf.fit(X_train, Y_train)

    print "Accuracy on training set."
    print clf.score(X_train, Y_train)
    print "Accuracy on testing set."
    print clf.score(X_test, Y_test)
    
    y_pred = clf.predict(X_test)

    print "Classification Report"
    print metrics.classification_report(Y_test, y_pred)
    print "Confusion Matrix:"
    print metrics.confusion_matrix(Y_test, y_pred)

#train_and_evaluate(clf, X_train, X_test, Y_train, Y_test)


glasses = [(10, 19), (30, 32), (37, 38), (50, 59), (63, 64),
        (69, 69), (120, 121), (124, 129), (130, 139), (160, 161),
        (164, 169), (180, 182), (185, 185), (189, 189), (190, 192),
        (194, 194), (196, 199), (260, 269), (270, 279), (300, 309),
        (330, 339), (358, 359), (360, 369)]

def create_target(segments):
    y = np.zeros(faces.target.shape[0])
    for (s, e) in segments:
        y[s: e + 1] = 1
    return y

target_glasses = create_target(glasses)

X_train, X_test, Y_train, Y_test = train_test_split(faces.data, target_glasses, test_size = 0.25, random_state = 0)

svc_2 = SVC(kernel = 'linear')
#evaluate_cross_validation(svc_2, X_train, Y_train, 5)
#train_and_evaluate(svc_2, X_train, X_test, Y_train, Y_test)

X_test = faces.data[30:40]
Y_test = target_glasses[30:40]

select = np.ones(target_glasses.shape[0])
select[30:40] = 0
X_train = faces.data[select == 1]
Y_train = target_glasses[select == 1]

svc_3 = SVC(kernel='linear')
train_and_evaluate(svc_3, X_train, X_test, Y_train, Y_test)
y_pred = svc_3.predict(X_test)

eval_faces = [np.reshape(a, (64,64)) for a in X_test]
print_faces(eval_faces, y_pred, 10)
print_faces(eval_faces, Y_test, 10)
