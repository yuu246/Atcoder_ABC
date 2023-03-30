#!/usr/bin/env python3

import copy
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
H, W, N, h, w = map(int, input().split())
graph = [[]]
for i in range(H):
    A = [0] + list(map(int, input().split()))
    graph.append(A)

ans = [[0] * (W-w+1) for i in range(H-h+1)]

memo = defaultdict(int)
for y in range(1, H+1):
    for x in range(1, W+1):
        memo[graph[y][x]] += 1

for k in range(H-h+1):
    for L in range(W-w+1):
        tmp = copy.deepcopy(memo)
        for i in range(k+1, k+h+1):
            for j in range(L+1, L+w+1):
                tmp[graph[i][j]] -= 1
                if tmp[graph[i][j]] == 0:
                    del tmp[graph[i][j]]
        key = set(tmp.keys())
        ans[k][L] = len(key)

for k in range(H-h+1):
    print(*ans[k])
