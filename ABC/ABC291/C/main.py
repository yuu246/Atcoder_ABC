#!/usr/bin/env python3
N = int(input())

S = list(input())

ans = True

dist = [[0, 0]]
X = 0
Y = 0
for i in range(N):
    if S[i] == 'R':
        X += 1
    if S[i] == 'L':
        X -= 1
    if S[i] == 'U':
        Y += 1
    if S[i] == 'D':
        Y -= 1
    dist.append([X, Y])

A = len(dist)
B = len(list(map(list, set(map(tuple, dist)))))
if A == B:
    print('No')
else:
    print('Yes')
