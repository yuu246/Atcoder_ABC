#!/usr/bin/env python3

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
B = set(A)
C = list(B)

i = 0
D = len(C)
K = min(D, K)
while i < K:
    if C[i] == i:
        i += 1
        if i == K:
            print(i)
            break
    else:
        print(i)
        break
