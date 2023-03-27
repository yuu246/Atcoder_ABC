#!/usr/bin/env python3
N = int(input())

money = 0
if N == 1:
    print(1)
else:
    for i in range(1, N):
        money += i
        if money >= N:
            print(i)
            break
