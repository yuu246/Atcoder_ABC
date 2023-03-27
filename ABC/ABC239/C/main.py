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
DIR = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
a, b, c, d = map(int, input().split())
set1 = set()
set2 = set()
dis = (a-c)**2 + (b-d)**2
if dis <= 20:
    for x, y in DIR:
        set1.add((a+x, b+y))
        set2.add((c+x, d+y))
    if set1 & set2:
        print('Yes')
        exit()

print('No')
