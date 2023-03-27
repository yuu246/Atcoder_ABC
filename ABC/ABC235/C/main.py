#!/usr/bin/env python3

from collections import defaultdict
N, Q = map(int, input().split())

A_list = list(map(int, input().split()))
Counter = defaultdict(list)
for i in range(N):
    Counter[A_list[i]].append(i+1)

for i in range(Q):
    x, k = map(int, input().split())
    k_list = Counter[x]
    if len(k_list) < k:
        print(-1)
    else:
        print(k_list[k-1])
