#!/usr/bin/env python3

a, b, c = map(int, input().split())

tmp1 = a + b
tmp2 = b + c
tmp3 = c + a

ans = max(tmp1, tmp2, tmp3)
print(ans)
