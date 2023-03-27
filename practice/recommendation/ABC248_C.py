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
mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
# dp[i][k]で表現すればワンちゃん
N, M, K = map(int, input().split())

dp = [[0 for i in range(K+1)] for i in range(N+1)]

for x in range(1, M+1):
    dp[1][x] = 1

for n in range(1, N):
    for k in range(1, K+1):
        for m in range(1, M+1):
            if k + m <= K:
                dp[n+1][k+m] += dp[n][k]
                dp[n+1][k+m] %= mod
ans = sum(dp[N]) % mod
print(ans)
