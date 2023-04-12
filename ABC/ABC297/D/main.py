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
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
A, B = map(int, input().split())

if A % B == 0:
    print(A//B - 1)
    exit()
if B % A == 0:
    print(B // A - 1)
    exit()


def gcd(x, y, cnt):
    if y == 0:
        return x, cnt
    else:
        if x % y == 0:
            adc = x // y - 1
        else:
            adc = x // y
        return gcd(y, x % y, cnt+adc)


if B > A:
    A, B = B, A

gc, cnt = gcd(A, B, 0)

print(cnt)
