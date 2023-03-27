#!/usr/bin/env python3

N = int(input())

mountain = []

for _ in range(N):
    s, t = input().split()
    t = int(t)
    mountain.append([s, t])

mountain.sort(reverse=True, key=lambda x:x[1])

print(mountain[1][0])