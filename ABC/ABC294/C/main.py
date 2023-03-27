#!/usr/bin/env python3

from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans_A = [0 for i in range(N)]
ans_B = [0 for i in range(M)]

A_Q = deque(A)
B_Q = deque(B)

idx = 0
idx_A = 0
idx_B = 0

while True:
    idx += 1
    if idx_A < N and idx_B < M:
        a = A_Q.popleft()
        b = B_Q.popleft()
        if a < b:
            B_Q.appendleft(b)
            ans_A[idx_A] = idx
            idx_A += 1
        else:
            A_Q.appendleft(a)
            ans_B[idx_B] = idx
            idx_B += 1
    elif idx_A < N:
        ans_A[idx_A] = idx
        idx_A += 1
    elif idx_B < M:
        ans_B[idx_B] = idx
        idx_B += 1
    else:
        break

print(*ans_A)
print(*ans_B)
