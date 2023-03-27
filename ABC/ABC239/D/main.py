#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect, bisect_left, bisect_right
import sys
def input(): return sys.stdin.readline().rstrip()


def is_ok(mid):
    if mid > 0:
        return True
    else:
        return False


def binary_search(ok, ng):
    # 複雑な二部探索用
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


INF = float('inf')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
prime = []
for i in range(2, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

flag = True
A, B, C, D = map(int, input().split())
for x in range(A, B+1):
    sita = x + C
    ue = x + D
    left = bisect_left(prime, sita)
    right = bisect_right(prime, ue)
    if left == right:
        flag = False

if flag:
    print('Aoki')
else:
    print('Takahashi')
