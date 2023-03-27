#!/usr/bin/env python3
from collections import Counter
senkyo = []
N = int(input())

for i in range(N):
    name = input()
    senkyo.append(name)

mycounter = Counter(senkyo)
ans = list(mycounter.most_common(1))
print(ans[0][0])
