#!/usr/bin/env python
# coding=utf-8

import numpy as np
import numpy.random 
import matplotlib.pyplot as plt
import scipy.stats

N = (np.arange(5) + 1) ** 2
print N
M = 10000

betaCLT = np.zeros((len(N), M), dtype=float)

for idx, x in enumerate(N):
    for j in xrange(M):
        betaCLT[idx, j] = (np.mean(numpy.random.beta(2, 1, x)) - 2.0 / 3) * np.sqrt(x) * 6.0 / np.sqrt(2)

fig, ax = plt.subplots(figsize=(10, 4))

for i in xrange(len(N)):
    density = k(betaCLT[i, :])
    xs = np.linspace(-5, 5, 200)
    density.covariance_factor = lambda : .15
    density._compute_covariance()
    ax.plot(xs, density(xs), lw=2, label = 'N = {0:>3}'.format(N[i]))

ax.plot(xs, scipy.stats.norm().pdf(xs), lw=2, label = 'normal distribution')
ax.legend(loc=3)

plt.show()
