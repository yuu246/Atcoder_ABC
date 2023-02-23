#!/usr/bin/env python3
N, K = map(int, input().split())
S = input()
T = ''

count = 0
i = 0
while count < K:
    if S[i] == 'o':
        T += 'o'
        count += 1
    else:
        T += 'x'
    i += 1

for i in range(N-len(T)):
    T += 'x'
print(T)
