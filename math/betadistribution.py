#!/usr/bin/env python
# coding=utf-8

import numpy as np
import numpy.random as nprnd
import scipy.stats as spstat
import scipy.special as ssp
import itertools as itt
import matplotlib.pyplot as plt
import pylab as pl


N = (np.arange(200) + 3) ** 2 * 20

betamean = np.zeros_like(N, dtype=float)

for idx, i in enumerate(N):
    betamean[idx] = np.mean(nprnd.beta(1, 1, i))

plt.plot(N, betamean, color='steelblue', lw=2)
plt.xscale('log')
plt.show()
