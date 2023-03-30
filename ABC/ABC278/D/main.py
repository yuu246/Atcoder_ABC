#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
import bisect
import sys


def input(): return sys.stdin.readline().rstrip()


def is_prime(x):
    # 素数判定
    LIMIT = int(x ** 0.5)
    for i in range(2, LIMIT + 1):
        if x % i == 0:
            return False
    return True


def is_ok(mid):
    if mid > 0:
        return True
    else:
        return False


def binary_search(ok, ng):
    # 複雑な二部探索用
    # 半開区間
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


INF = float('inf')

# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d = defaultdict(int)
flag = False
for i in range(Q):
    a, *b = map(int, input().split())
    if a == 1:
        base = b[0]
        d = defaultdict(int)
        flag = True
    if a == 2:
        d[b[0]-1] += b[1]
    if a == 3:
        if flag:
            print(base + d[b[0]-1])
        else:
            print(A[b[0]-1] + d[b[0]-1])
