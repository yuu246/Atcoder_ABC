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
N = int(input())
A = list(map(int, input().split()))
B = A.reverse()
sum = [0 for i in range(N+1)]
for i in range(1, N+1):
    sum[i] = A[N-i] + sum[i-1]

ans_list = []
for x in sum:
    ans_list.append(x % 360)
ans_list.append(360)
ans_list.sort()
length = len(ans_list)
ans = -1
for i in range(length-1):
    tmp = ans_list[i+1] - ans_list[i]
    ans = max(ans, tmp)

print(ans)
