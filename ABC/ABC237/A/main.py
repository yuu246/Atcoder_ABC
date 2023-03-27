#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect
import sys
def input(): return sys.stdin.readline().rstrip()


INF = float('inf')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
jouken = 2**31
N = int(input())
if -1 * jouken <= N < jouken:
    print('Yes')
else:
    print('No')
