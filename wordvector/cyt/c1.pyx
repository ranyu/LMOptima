import math
cimport numpy as np
import numpy as np

cdef extern from "math.h":
    float pow(double x,double y)

'''cdef float _great_circle(float lon1,float lat1,float lon2,float lat2):
    cdef float radius = 3956.0
    cdef float pi = 3.14159265
    cdef float x = pi/180.0
    cdef float a,b,theta,c

    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = acosf((cosf(a)*cosf(b)) + (sinf(a)*sinf(b)*cosf(theta)))
    return radius*c'''
cdef double _inner_product(np.ndarray[double,ndim=1] a1,np.ndarray[double,ndim=1] a2,int fre,double p1,double p2):
    cdef double sum = 0
    cdef int i = 0
    cdef int length = a1.size
    cdef double e1 = 0
    cdef double e2 = 0
    cdef double result = 0
    for i in xrange(length):
        e1 = a1[i]
        e2 = a2[i]
        sum += e1 * e2
    result = pow(fre,p1)*pow(sum+2,p2)  
    return result

'''def great_circle(float lon1,float lat1,float lon2,float lat2,int num):
    cdef int i  
    cdef float x  
    for i from 0 <= i < num:
        x = _great_circle(lon1,lat1,lon2,lat2)  
    return x'''  

def inner_product(np.ndarray[double,ndim=1] a1,np.ndarray[double,ndim=1] a2,fre,p1,p2):
    cdef double result = 0
    result = _inner_product(a1,a2,fre,p1,p2)
    return result

