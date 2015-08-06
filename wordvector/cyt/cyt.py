#!/usr/bin/env python
# coding=utf-8

import timeit  
import c1

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000

t = timeit.Timer("c1.great_circle(%f,%f,%f,%f,%d)" % (lon1,lat1,lon2,lat2,num),
                                        "import c1")
print c1.great_circle(lon1,lat1,lon2,lat2,1)
print "Cython function", t.timeit(1), "sec"
