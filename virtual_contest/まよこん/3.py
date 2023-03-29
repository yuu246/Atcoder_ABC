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
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())
graph = []
for i in range(N):
    A = list(map(int, list(input())))
    graph.append(A)


def tansaku(x, y):
    kouho = -10
    for i, j in DIR:
        tmp = graph[x][y]
        x2 = x
        y2 = y
        for _ in range(N-1):
            x2 += i
            y2 += j
            if x2 < 0:
                x2 = N-1
            if x2 > N-1:
                x2 = 0
            if y2 < 0:
                y2 = N-1
            if y2 > N-1:
                y2 = 0
            tmp *= 10
            tmp += graph[x2][y2]
        kouho = max(kouho, tmp)
    return kouho


ans = -10
for i in range(N):
    for j in range(N):
        ans = max(ans, tansaku(i, j))

print(ans)
