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


def check(y, x):
    tmp_y = 0
    tmp_x = 0
    tmp_xy = 0
    tmp_yx = 0
    if y <= N-6:
        for i in range(6):
            if graph[y+i][x] == '#':
                tmp_y += 1
    if x <= N-6:
        for i in range(6):
            if graph[y][x+i] == '#':
                tmp_x += 1
    if y <= N-6 and x <= N-6:
        for i in range(6):
            if graph[y+i][x+i] == '#':
                tmp_xy += 1
            if graph[y+5-i][x+i] == '#':
                tmp_yx += 1
    if tmp_x >= 4 or tmp_y >= 4 or tmp_xy >= 4 or tmp_yx >= 4:
        return True
    else:
        return False


graph = []
N = int(input())
for i in range(N):
    S = list(input())
    graph.append(S)

for i in range(N):
    for j in range(N):
        if check(i, j):
            print('Yes')
            exit()
print('No')
