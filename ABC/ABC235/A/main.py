#!/usr/bin/env python3
x = input()
x1 = x
x2 = x[1:] + x[:1]
x3 = x[2:] + x[:2]
ans = int(x1) + int(x2) + int(x3)
print(ans)
