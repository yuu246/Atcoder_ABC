#!/usr/bin/env python3

import math
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
N = int(input())
C = [0] + list(map(int, input().split()))
Q = int(input())
sell_2 = 0
sell_3 = 0
odd_min = 10**10
all_min = 10**10
odd_count = 0
for i in range(1, N+1, 2):
    odd_count += 1
    odd_min = min(C[i], odd_min)
for i in range(1, N+1):
    all_min = min(all_min, C[i])
ans = 0
for _ in range(Q):
    i, *S = map(int, input().split())
    if i == 1:
        x = S[0]
        if x % 2 == 0:
            if C[x] - sell_3 >= S[1]:
                ans += S[1]
                C[x] -= S[1]
                if all_min >= (C[x] - sell_3):
                    all_min = (C[x] - sell_3)
        else:
            if C[x] - sell_2 - sell_3 >= S[1]:
                ans += S[1]
                C[x] -= S[1]
                if all_min >= (C[x] - sell_2-sell_3):
                    all_min = (C[x]-sell_2-sell_3)
                if odd_min >= (C[x]-sell_2-sell_3):
                    odd_min = (C[x]-sell_2-sell_3)
    if i == 2:
        if odd_min >= S[0]:
            sell_2 += S[0]
            odd_min -= S[0]
            if odd_min < all_min:
                all_min = odd_min
    if i == 3:
        if all_min >= S[0]:
            sell_3 += S[0]
            all_min -= S[0]
            odd_min -= S[0]
ans += sell_2 * odd_count + sell_3 * N
print(ans)
