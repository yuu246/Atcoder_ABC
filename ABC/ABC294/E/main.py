#!/usr/bin/env python3
L, N1, N2 = map(int, input().split())
X1 = []
X2 = []
for i in range(N1):
    v, l_ = map(int, input().split())
    tmp = [v for i in range(l_)]
    X1 += tmp

for i in range(N2):
    v, l_ = map(int, input().split())
    tmp = [v for i in range(l_)]
    X2 += tmp
