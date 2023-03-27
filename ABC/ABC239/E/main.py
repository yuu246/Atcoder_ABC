#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect
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

N, Q = map(int, input().split())
X = [0] + list(map(int, input().split()))

graph = [list() for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans_list = [0]


def dfs(v, v_):
    visited = set()
    visited.add(v_)
    Q = deque()
    Q.append(v)
    while len(Q) > 0:
        x = Q.pop()
        visited.add(x)
        for y in graph[x]:
            if y not in visited:
                Q.append(y)
    return visited


for i in range(Q):
    v, k = map(int, input().split())
    if v == 1:
        import copy
        X2 = copy.deepcopy(X)
        X2.sort(reverse=True)
        print(X2[k-1])
        continue
    ans_set = set()
    ans_set.add(v)
    for v_ in graph[v]:
        visited = dfs(v_, v)
        if 1 not in visited:
            ans_set = ans_set.union(visited)

    ans_list = list(ans_set)
    ans = []
    for x in ans_list:
        ans.append(X[x])
    ans.sort(reverse=True)

    print(ans[k-1])
