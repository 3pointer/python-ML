#!/usr/bin/env python
# coding=utf-8

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

x = np.random.rand(1e5)

xs = np.linspace(-0.2 , 1.2, 300)

desity = ss.gaussian_kde(x)

desity.covariance_factor = lambda :  0.02

desity._compute_covariance()

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(xs, desity(xs), lw = 3, color = 'red', label = u'moni')
ax.plot(xs, ss.uniform().pdf(xs), lw = 3, color = 'blue', label = u'real')

plt.show()
