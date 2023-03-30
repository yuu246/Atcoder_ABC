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
H, M = map(int, input().split())


def is_ok(H, M):
    return 0 <= H <= 23 and 0 <= M <= 59


def check(H, M):
    A, B = H // 10, H % 10
    C, D = M // 10, M % 10
    x = A*10+C
    y = B*10+D
    return is_ok(x, y)


while True:
    if check(H, M):
        print(H, M)
        exit()
    M += 1
    if M == 60:
        H, M = H+1, 0
    if H == 24:
        H = 0
