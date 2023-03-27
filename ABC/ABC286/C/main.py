#!/usr/bin/env python3

from collections import deque
N, A, B = map(int, input().split())
S = input()


S = list(S)
S = deque(S)

ans = 10**12

for Ac in range(N):
    for _ in range(Ac):
        sf = S.popleft()
        S.append(sf)
    Bc = 0
    for k in range(N // 2):
        if S[k] != S[N-1-k]:
            Bc += 1
    ans = min(A*Ac+B*Bc, ans)

print(ans)
