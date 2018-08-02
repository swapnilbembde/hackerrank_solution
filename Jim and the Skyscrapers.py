#!/bin/python
#https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem
from __future__ import print_function

import os

# Complete the solve function below.
def solve(arr):
    
    dc={}
    head=arr[0]
    dc[arr[0]]=1
    paths=0
    for i in range(1,len(arr)):
        if arr[i] not in dc.keys():
            dc[arr[i]]=1
        else:
            dc[arr[i]]+=1

        if arr[i]>arr[i-1]:
            head=arr[i]
            for j in sorted(dc.keys()):
                if j < head :
                    paths+=dc[j]*(dc[j]-1)
                    del dc[j]
                else: break    
                
    for i in dc.keys():
        paths+=dc[i]*(dc[i]-1)
    #print(paths)
    return paths
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
