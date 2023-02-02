#!/usr/bin/env python3

N = int(input())
S = []
T = []
for _ in range(N):
    s, t = map(str, input().split())
    S.append(s)
    T.append(t)

def change(num):
    visited[num] = True
    x = S[num]
    if x in T:
        k = T.index(x)
        change(k)


visited = [False] * N

setS = set(S)
setT = set(T)
difference_list = setT.difference(setS)

if len(difference_list) == 0:
    print('No')
else:
    for diff in difference_list:
        j = T.index(diff)
        change(j)
    # print(visited)
    if False in visited:
        print('No')
    else:
        print('Yes')