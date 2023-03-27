#!/usr/bin/env python3
N = int(input())
T = input()
N2 = 2*N
f = False
for i in range(N2):
    a = T[:i]
    S = T[i:N+i]
    b = T[N+i:]
    if a + b == S[::-1]:
        print(a + b)
        print(i)
        f = True
        break

if not f:
    print(-1)
