#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swap = 0
    for i in range(len(q)-1,-1,-1):
        if q[i]-(i+1)>2:
            print("Too chaotic")
            return
        else:
            j = max(0,q[i]-2)
            while(j<i):
                if (q[j]>q[i]):
                    swap +=1
                j +=1
    print(swap)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
