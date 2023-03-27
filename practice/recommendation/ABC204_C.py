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

graph = [list() for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = 0
for start in range(1, N+1):
    Q = deque()
    visited = set()
    Q.append(start)
    while len(Q) > 0:
        x = Q.pop()
        visited.add(x)
        for y in graph[x]:
            if y not in visited:
                Q.append(y)
    ans += (len(visited))

print(ans)
