from __future__ import print_function
import numpy as np
import random

# Our function is y = 5x.
x_train = np.arange(0, 100)
y_train = x_train * 5
m = random.random()
a = 0.01

for epoch in range(0, 10):
    for i in range(0, len(x_train)):
        x = x_train[i]
        y = y_train[i]
        computed = x * m
        diff = computed - y
        m -= diff * a * x

print("Final weight: " + str(m))
print("Expected weight: 5.0")
