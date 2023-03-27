#!/usr/bin/env python3
from collections import defaultdict

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

stations = defaultdict(int)

for i in range(N):
    stations[S[i]] += 1

for i in range(M):
    stations[T[i]] += 1

for station in S:
    if stations[station] == 2:
        print('Yes')
    else:
        print('No')
