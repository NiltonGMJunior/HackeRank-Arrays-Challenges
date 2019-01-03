#!/bin/python3

import math
import os
import random
import re
import sys


def minimumBribes(q):
    swaps = [0]*len(q)
    for index, elem in enumerate(q):
        swaps[elem - 1] = elem - 1 - index
    if any(list(map(lambda s: s > 2, swaps))):
        print("Too chaotic")
    else:
        min_swaps = sum(list(filter(lambda t: t > 0, swaps)))
        print(min_swaps)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
