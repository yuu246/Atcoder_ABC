#!/usr/bin/env python3

N, Q = map(int, input().split())
player = [0] * (N+1)

for i in range(Q):
    x, y = map(int, input().split())

    if x == 1:
        player[y] += 1

    if x == 2:
        player[y] += 2
    if x == 3:
        if player[y] >= 2:
            print('Yes')
        else:
            print('No')
