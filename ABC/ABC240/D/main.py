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


def delete(Q, ans, front, cont):
    for i in range(cont):
        Q.pop()
    ans -= cont
    if ans == 0:
        return Q, ans, 0, 0
    front = Q[-1]
    cont = 1
    while cont < ans and Q[-1*cont - 1] == front:
        cont += 1
    return Q, ans, front, cont


N = int(input())

A = list(map(int, input().split()))
Q = deque()
front = 0
cont = 0
ans = 0
for idx in range(N):
    x = A[idx]
    ans += 1
    Q.append(x)
    if front == x:
        cont += 1
    else:
        front = x
        cont = 1
    if cont == x:
        while cont == front and cont != 0:
            Q, ans, front, cont = delete(Q, ans, front, cont)
    print(ans)
