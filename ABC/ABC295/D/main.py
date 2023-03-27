#!/usr/bin/env python3

import math
from copy import deepcopy
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
S = list(input())
S = list(map(int, S))
counts = [0] * 1024
counts[0] = 1
tmp = 0

for i in range(len(S)):
    tmp ^= 1 << S[i]
    counts[tmp] += 1

ans = 0
for x in counts:
    ans += x * (x - 1) // 2
print(ans)
