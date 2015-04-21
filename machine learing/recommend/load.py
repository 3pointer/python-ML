#!/usr/bin/env python
# coding=utf-8

def LoadMatrix():
    matrix = {}
    file = open("train.csv")
    columns = file.readline().split(',')

    for line in file:
        scores = line.split(',')
        for i in range(len(scores))[1:]:
            matrix[(scores[0], columns[i])] = scores[i].strip("\n")
    return matrix

m = LoadMatrix()
print m
