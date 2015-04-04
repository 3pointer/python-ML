#!/usr/bin/env python
# coding=utf-8

from numpy import *
import os
import re

times = ['2014-11-18','2014-11-19','2014-11-20' ,'2014-11-21','2014-11-22','2014-11-23','2014-11-24','2014-11-25','2014-11-26','2014-11-27','2014-11-28','2014-11-29','2014-11-30','2014-12-01','2014-12-02','2014-12-03','2014-12-04','2014-12-05','2014-12-06','2014-12-07','2014-12-08','2014-12-09','2014-12-10','2014-12-11','2014-12-13','2014-12-14','2014-12-15','2014-12-16','2014-12-17','2014-12-18']

pat1 = '../../'

N = 7

"""
def getData(vis, filepath):
                userid = j
                j = os.path.join(filepath, j)
                if os.path.isfile(j):
                    cou = -1
                    file = open(j, 'r')            
                    for line in file:
                        cou += 1
                        #print line
                        p = re.compile(r'\d+')
                        line = p.findall(line)
                        if line[1] in vis:
                            vis.setdefault(line[1], cou);
                    file.close()
                    pass
                    """
def behaviourToTrainData(numday):
    vis = {}
    for i in xrange(numday - N, numday - 1):
        sourceDir = os.path.join(pat1, times[i])        
        if not os.path.exists(sourceDir):
            print 'not find dir in pat1'
            #print sourceDir
        trainData = getData(vis, sourceDir) 
        pass

def behaviourToTrainTarget(userid, numday):
    pass


def main():
    len = times.__len__()
    for i in xrange(N, len - N - 1):
        userid, trainData = behaviourToTrainData(i)
        trainTarget = behaviourToTrainTarget(i)

        pass
behaviourToTrainData(7)
