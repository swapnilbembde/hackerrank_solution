#!/bin/python
#https://www.hackerrank.com/challenges/contacts/problem
from __future__ import print_function

import os
import sys

loop = int(raw_input())

m = {}

def add_word(word):
    for i in range(1, len(word)+1):
        if word[:i] in m:
            m[word[:i]] += 1
        else:
            m[word[:i]] = 1
            
def find_partial(word):
    return m.get(word) or 0

for i in range(loop):
    inputs = raw_input().split()
    
    if inputs[0] == "add":
        add_word(inputs[1])
    else:
        print (find_partial(inputs[1]))
