#!/usr/bin/env python3
from math import factorial


def nCr(n, r):
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return numerator // denominator


A, B, K = map(int, input().split())

ans = ''
num = 1

while A > 0 or B > 0:
    if A == 0:
        ans += 'b'
        B -= 1
        continue
    if B == 0:
        ans += 'a'
        A -= 1
        continue

    b_start = num + nCr(A-1+B, B)

    if b_start > K:
        ans += 'a'
        A -= 1

    else:
        ans += 'b'
        B -= 1
        num = b_start

print(ans)
