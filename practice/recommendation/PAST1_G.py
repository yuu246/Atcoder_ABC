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
A = []
for i in range(N-1):
    lst = list(map(int, input().split()))
    A.append([0]*(i+1) + lst)

ALL = 1 << N
happy = [0]*ALL


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(N):
        for j in range(i+1, N):
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]

ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        if n1 & n2 > 0:
            continue

        n3 = ALL-1 - (n1 | n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)
