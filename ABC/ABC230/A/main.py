#!/usr/bin/env python3

N = int(input())
if N >= 42:
    N += 1

if N <= 9:
    N = str(N)
    ans = 'AGC00' + N
else:
    N = str(N)
    ans = 'AGC0' + N
print(ans)
