#!/usr/bin/env python3
from itertools import product
from collections import Counter
H, W = map(int, input().split())
ans = 0

graph = [[]]
for i in range(H):
    side = [-1] + list(map(int, input().split()))
    graph.append(side)

ans_set = set()

for bits in product([0, 1], repeat=H+W-2):
    C = Counter(bits)
    if C[0] == H - 1:
        ans_set.add(bits)

ans_list = list(ans_set)
for comb in ans_list:
    tmp_set = set()
    x = 1
    y = 1
    tmp_set.add(graph[x][y])
    for i in range(H+W-2):
        if comb[i] == 0:
            x += 1
            tmp_set.add(graph[x][y])
        if comb[i] == 1:
            y += 1
            tmp_set.add(graph[x][y])
    if len(tmp_set) == H+W-1:
        ans += 1

print(ans)
