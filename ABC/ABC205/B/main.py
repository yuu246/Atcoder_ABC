#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(1, N+1):
    if A[i-1] != i:
        print('No')
        break
else:
    print('Yes')
