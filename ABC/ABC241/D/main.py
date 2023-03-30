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
Q = int(input())
A = deque()


def q1(x):
    iti = bisect.bisect_right(A, x)
    A.insert(iti, x)


def q2(x, k):
    iti = bisect.bisect_right(A, x)
    if iti-k >= 0:
        print(A[iti-k])
    else:
        print(-1)


def q3(x, k):
    iti = bisect.bisect_left(A, x)
    if iti+k-1 <= len(A)-1:
        print(A[iti+k-1])
    else:
        print(-1)


for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q1(query[1])
    elif query[0] == 2:
        q2(query[1], query[2])
    else:
        q3(query[1], query[2])
