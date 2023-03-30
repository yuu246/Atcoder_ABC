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
mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())
dp = [[0]*10 for i in range(N+1)]

for x in range(1, 10):
    dp[1][x] = 1

for y in range(2, N+1):
    for x in range(1, 10):
        if x == 1:
            dp[y][x] += (dp[y-1][x] + dp[y-1][x+1])
        elif x == 9:
            dp[y][x] += (dp[y-1][x-1] + dp[y-1][x])
        else:
            dp[y][x] += (dp[y-1][x-1] + dp[y-1][x] + dp[y-1][x+1])
        dp[y][x] %= mod

ans = 0
for i in range(1, 10):
    ans += dp[N][i]
    ans %= mod
print(ans)
