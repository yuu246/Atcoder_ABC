#!/usr/bin/env python3


N = int(input())
S_list = []
for i in range(N):
    s = input()
    S_list.append([s, i])

sorted_list = sorted(S_list)

ans = [0] * N

for i in range(N):
    count = 0
    if i == 0:
        pass
    elif i == N-1:
        pass
    else:
        for j in range(min(len(s[i][0]), len(s[i - 1][0]))):
            if s[i][0][j] != s[i - 1][0][j]:
                count = max(count, j)
            if s[i][0][j] != s[i + 1][0][j]:
                count = max(count, j)
                


