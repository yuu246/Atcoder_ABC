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
mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())
length = len(str(N)) - 1

hikuyatu = [0] + [0 for i in range(length)] + [0]

if length > 0:
    while True:
        nine = '9' * length
        hikuyatu[length] = N - int(nine) - hikuyatu[length + 1]
        length -= 1
        if length == 0:
            break

ans = (1+N) * N // 2
for idx, counter in enumerate(hikuyatu):
    atai = '9' * idx
    if atai == '':
        continue
    atai = int(atai)
    ans -= (int(atai) * counter) % mod
    if ans < 0:
        ans += mod

print(ans)
