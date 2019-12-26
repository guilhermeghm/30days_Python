#!/bin/python3

import math
import os
import random
import re
import sys

#To define if it is odd or even
# 0 = odd
# 1 = even
def module(N):
    mod = N % 2
    if mod > 0:
        check = 0
    else:
        check = 1
    return check

def number(N,check):
    if N in range(1,6) and check==1:
        print ("Not Weird")
    elif N in range(1,6) and check==0:
        print ("Weird")
    elif N in range (5,21) and check==1:
        print ("Weird")
    elif N > 20 and check==1:
        print ("Not Weird")
    elif N > 20 and check==0:
        print ("Weird")
    elif check==1:
        print ("Weird")


if __name__ == '__main__':
    N = int(input())
    x=module(N)
    number(N,x)

