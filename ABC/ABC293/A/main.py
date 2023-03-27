#!/usr/bin/env python3

S = list(input())
length = len(S)
for i in range(0, length-1, 2):
    S[i+1], S[i] = S[i], S[i+1]

ans = ''.join(S)
print(ans)
