#!/usr/bin/env python3

A, B, C = map(int, input().split())

if C % 2 == 0:
    if abs(A) > abs(B):
        ans = '>'
    elif abs(A) == abs(B):
        ans = '='
    else:
        ans = '<'
else:
    if A > B:
        ans = '>'
    elif A == B:
        ans = '='
    else:
        ans = '<'

print(ans)
