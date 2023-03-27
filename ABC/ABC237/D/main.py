#!/usr/bin/env python3

from itertools import product, permutations, combinations, combinations_with_replacement
import heapq
from collections import deque, defaultdict, Counter
from bisect import bisect
import sys
def input(): return sys.stdin.readline().rstrip()


INF = float('inf')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(10**9)

#  -----------------------  #
N = int(input())
S = input()

ans = deque()
ans.append(N)

for i in range(N-1, -1, -1):
    if S[i] == 'R':
        ans.appendleft(i)
    else:
        ans.append(i)

print(*ans)
# Left = deque()
# Right = deque()

# for i, c in enumerate(S):
#     if c == 'R':
#         Left.append(i)
#     if c == 'L':
#         Right.appendleft(i)
# a_n = deque()
# a_n.append(N)
# ans = Left + a_n + Right
# print(*ans)
