#!/usr/bin/env python
# coding=utf-8


from sklearn.datasets import fetch_olivetti_faces
import matplotlib
import matplotlib.pyplot as plt

faces = fetch_olivetti_faces()

def print_faces(images, target, top_n):
    fig = plt.figure(figsize=(12, 12))
    fig.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1, hspace = 0.05, wspace = 0.05)
    
    for i in range(top_n):
        p = fig.add_subplot(20, 20, i + 1, xticks = [], yticks = [])
        p.imshow(images[i], cmap=plt.cm.bone)

        #p.text(0, 14, str(target[i]))
        #p.text(0, 60, str(i))


print_faces(faces.images, faces.target, 200)
plt.show()

