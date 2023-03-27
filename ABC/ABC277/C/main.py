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
query = defaultdict(list)
visited = defaultdict(int)
Q = deque()
for _ in range(N):
    a, b = map(int, input().split())
    query[a].append(b)
    query[b].append(a)


def dfs(x):
    global high
    if visited.get(x) is None:
        visited[x] += 1
        for y in query[x]:
            if visited.get(y) is None:
                high = max(y, high)
                dfs(y)


high = 1
dfs(1)
print(high)
