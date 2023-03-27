#!/usr/bin/env python3
N = int(input())

math = []
for i in range(N):
    a, b = map(int, input().split())
    math.append(a + b)

for x in math:
    print(x)