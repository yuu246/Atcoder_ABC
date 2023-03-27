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
N, X = map(int, input().split())
jumps = [[]]
for i in range(N):
    jump = list(map(int, input().split()))
    jumps.append(jump)

dp = [[False for i in range(X+1)] for j in range(N+1)]

a, b = jumps[1]
if a <= X and b <= X:
    dp[1][jumps[1][0]] = True
    dp[1][jumps[1][1]] = True
elif a <= X:
    dp[1][a] = True
elif b <= X:
    dp[1][b] = True
else:
    print('No')
    exit()

for i in range(2, N+1):
    a, b = jumps[i]
    for j in range(1, X+1):
        if 0 <= j-a <= X and 0 <= j-b <= X:
            if dp[i-1][j-a] or dp[i-1][j-b]:
                dp[i][j] = True
        elif 0 <= j-a <= X:
            if dp[i-1][j-a]:
                dp[i][j] = True
        elif 0 <= j-b <= X:
            if dp[i-1][j-b]:
                dp[i][j] = True

if dp[N][X]:
    print('Yes')
else:
    print('No')
