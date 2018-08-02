#!/bin/python
#https://www.hackerrank.com/challenges/x-and-his-shots/problem

from __future__ import print_function

import os
import sys

# Complete the solve function below.
def solve(shots, players):
    count =0
    for i in players:
        for j in shots:
            if(j[1]<i[0] or j[0]>i[1]):
                count+=1
    #print(len(players)*len(shots) -count)
    return(len(players)*len(shots) -count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in xrange(n):
        shots.append(map(int, raw_input().rstrip().split()))

    players = []

    for _ in xrange(m):
        players.append(map(int, raw_input().rstrip().split()))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
