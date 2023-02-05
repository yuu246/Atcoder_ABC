#!/usr/bin/env python3
N, K = map(int, input().split())

names = []
for _ in range(N):
    name = input()
    names.append(name)

K_names = names[:K]
K_names.sort()
for _ in range(K):
    print(K_names[_])

