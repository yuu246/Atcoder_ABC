#!/usr/bin/env python3

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

B_Cj = [0] * (N + 1)
for i in range(1, N+1):
    B_Cj[i] = B[C[i]]

pop_time = [0] * (N+1)
for i in range(1, N+1):
    pop_time[A[i]] += 1

pop_time_B = [0] * (N+1)
for i in range(1, N+1):
    pop_time_B[B_Cj[i]] += 1

ans = 0

for i in range(1, N+1):
    ans += pop_time[i] * pop_time_B[i]

print(ans)
