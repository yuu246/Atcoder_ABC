#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect
import sys


def input(): return sys.stdin.readline().rstrip()
def list_int(): return list(map(int, input().split()))


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

# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())

points = [[]]
Array = defaultdict(int)

for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
    Array[(x, y)] += 1

ans = 0

for x in range(1, N+1):
    for y in range(x+1, N+1):
        x1, y1 = points[x]
        x2, y2 = points[y]
        if x1 == x2 or y1 == y2:
            continue
        if Array[(x2, y1)] and Array[(x1, y2)]:
            ans += 1


print(ans // 2)
