#!/usr/bin/env python3

L, R = map(int, input().split())

S = '0' + input()
A = S[1:L]
B = (S[R:L-1:-1])
C = S[R+1:]
ans = A + B + C
print(ans)
