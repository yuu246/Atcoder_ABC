#!/usr/bin/env python3
import numpy as np
from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect
import sys
def input(): return sys.stdin.readline().rstrip()


INF = float('inf')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
H, W = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(H)]
# B_graph = [[0 for j in range(W)] for i in range(H)]
# for i in range(H):
#     for j in range(W):
#         B_graph[j][i] = graph[i][j]
ans_list = np.array(graph).T.tolist()
for i in range(W):
    print(*ans_list[i])
