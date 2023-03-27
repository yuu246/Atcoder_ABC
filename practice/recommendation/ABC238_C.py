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
N = int(input())

ans = N * (N+1) // 2

ans %= mod
N_str = str(N)
counter = ''
minus = ''
for x in range(len(N_str)-1):
    if x == 0:
        minus += '9'
    else:
        minus += '0'
    counter += '9'
    total_minas = (N - int(counter)) * int(minus)
    ans -= total_minas % mod
    if ans < 0:
        ans += mod
print(ans)
