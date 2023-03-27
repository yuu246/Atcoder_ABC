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
R, C = map(int, input().split())
graph = []
for i in range(R):
    mapp = list(input())
    graph.append((mapp))

for y in range(R):
    for x in range(C):
        if graph[y][x] != '.' and graph[y][x] != '#':
            length = int(graph[y][x])
            for y2 in range(R):
                for x2 in range(C):
                    if abs(y2-y) + abs(x2-x) <= length and graph[y2][x2] == '#':
                        graph[y2][x2] = '.'
            graph[y][x] = '.'

for i in range(R):
    graph[i] = ''.join(graph[i])

print(*graph, sep='\n')
