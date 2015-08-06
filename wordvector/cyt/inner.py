#!/usr/bin/env python
# coding=utf-8

import c1
import numpy as np

a1 = np.array([10.0,11.0])
a2 = np.array([1.0,11.0])

print type(a1),a2
print c1.inner_product(a1,a2)
