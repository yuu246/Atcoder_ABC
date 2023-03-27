#!/usr/bin/env python3

N, M = map(int, input().split())

S_list = []
T_set = set()

for i in range(N):
    s = input()
    S_list.append(s)

for i in range(M):
    t = input()
    T_set.add(t)

ans = 0

for i in range(N):
    for j in T_set:
        if S_list[i].endswith(j):
            ans += 1

print(ans)
