#!/usr/bin/env python3
from collections import Counter
N = int(input())
A_list = list(map(int, input().split()))
dict_A = Counter(A_list)
for i in range(1, 4*N):
    if dict_A[i] == 3:
        print(i)
        break
