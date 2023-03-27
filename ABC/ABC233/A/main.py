#!/usr/bin/env python3

X, Y = map(int, input().split())

if (Y - X) <= 0:
    ans = 0
else:
    if (Y-X) % 10 == 0:
        ans = (Y - X) // 10
    else:
        ans = (Y - X) // 10 + 1
print(ans)
