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
N, M = map(int, input().split())
A = list_int()
sum_a = sum(A)
Q = defaultdict(int)
for x in A:
    Q[x] += 1

visited = defaultdict(int)
key = Q.keys()
key = list(key)

maxi = 0

for start in key:
    if not visited[start]:
        tmp = 0
        tmp += Q[start] * start
        maxi = max(maxi, tmp)
        visited[start] += 1
        next = start + 1
        while Q[next] and maxi != sum_a:
            visited[next] += 1
            tmp += Q[next] * next
            maxi = max(tmp, maxi)
            next += 1
            if next == M:
                next = 0
print(sum_a - maxi)
