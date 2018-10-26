# -*- coding: utf-8 -*


import matplotlib.pyplot as plt
import numpy as np
from filtering import WordCount


X, Y = [], []
for line in open('source_0_split_0__7L3Id.mtxt', 'r'):
    values = [float(s) for s in line.split()]
    X.append(values[0])
    Y.append(values[1])

plt.plot(X, Y)
plt.show()