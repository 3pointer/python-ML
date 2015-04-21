#!/usr/bin/env python
# coding=utf-8

import os
import sys
import scipy as sp

Dir = './text/'
from sklearn.feature_extraction.text import CountVectorizer


posts = [open(os.path.join(Dir, f)).read() for f in os.listdir(Dir)]
vectorizer = CountVectorizer(min_df = 1, stop_words = 'english')
X_train = vectorizer.fit_transform(posts)

def dis_raw(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

def main():
    num_samples, num_features = X_train.shape
    best_dist = sys.maxint
    best_i = None
    new_post = "imaging databases"
    new_post_vec = vectorizer.transform([new_post])
    for i in range(0, num_samples):
        post = posts[i]
        post_vec = X_train.getrow(i)
        d = dis_raw(post_vec, new_post_vec)
        print "=== Post %i with dist = %.2f: %s"%(i,d,post)
        if d < best_dist:
            best_i = i
            best_dist = d
    print "Best post is %i with dist=%.2f" %(best_i, best_dist)

main()




