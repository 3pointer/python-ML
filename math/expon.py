#!/usr/bin/env python
# coding=utf-8

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

x = np.random.rand(10)
x = -np.log(x)

xs = np.linspace(-0.2, 1.2, 300)
density = ss.gaussian_kde(x)
density.covariance_factor = lambda : 0.02
density._compute_covariance()
fig, ax = plt.subplots(figsize=(50,5))

ax.plot(xs, density(xs), lw = 1, color='red', label = 'moni')
ax.plot(xs, ss.expon().pdf(xs), lw = 1, color='blue', label = 'real')
plt.show()

