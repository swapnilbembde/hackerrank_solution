#!/bin/python
#https://www.hackerrank.com/challenges/components-in-graph/problem
from __future__ import print_function

import os
import sys

#
# Complete the componentsInGraph function below.
#
def fn(i):
    while arr[i] >= 0:
        if arr[arr[i]] >= 0:
            arr[i] = arr[arr[i]]
        i = arr[i]
    return i
    
def componentsInGraph(gb):
    # print (gb)
    for i in gb:
        i[0] = fn(i[0]-1)
        i[1] = fn(i[1]-1)
        if i[0]!=i[1]:
            if arr[i[0]] > arr[i[1]]:
                i[0],i[1] = i[1],i[0]
            arr[i[0]] = arr[i[0]] + arr[i[1]]
            arr[i[1]] = i[0]
    mn = 2*n
    mx = 0
    for i in range(2*n):
        if arr[i]<-1:
            mn= min(mn,-arr[i])
            mx= max(mx,-arr[i])
    # print(mn,mx)
    print(str(mn) + " " + str(mx))   
    
    # print (mn,mx)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    gb = []
    arr = [-1]*(2*n)
    for _ in xrange(n):
        gb.append(map(int, raw_input().rstrip().split()))

    result = componentsInGraph(gb)

#     fptr.write(' '.join(map(str, SPACE)))
#     fptr.write('\n')

#     fptr.close()
