import sys

with open(sys.argv[1],'r') as f:
    for data in f:
        print (data.strip().split()[0])
