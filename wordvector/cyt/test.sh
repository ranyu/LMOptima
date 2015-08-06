#!/bin/bash

cython c1.pyx

# Compile the object file
gcc -c -fPIC -I /usr/include/python2.6/ c1.c

# Link it into a shared library
gcc -shared c1.o -o c1.so
