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
S = input()

N = len(S)
if S == "a"*N:
    print("Yes")
    exit()

front_count = 0
back_count = 0
f_idx = -1
b_idx = -1
while True:
    f_idx += 1
    if S[f_idx] == 'a':
        front_count += 1
    else:
        break
part_S = S[front_count:]
part_S = part_S[::-1]

while True:
    b_idx += 1
    if part_S[b_idx] == 'a':
        back_count += 1
    else:
        break

final = part_S[back_count:]
flag = True

length = (len(S) - front_count-back_count)
for i in range(length // 2):
    if final[i] != final[length-1-i]:
        flag = False

if front_count > back_count:
    flag = False
if flag:
    print('Yes')
else:
    print('No')
