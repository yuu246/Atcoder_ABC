#!/usr/bin/env python3

x, y = map(int, input().split())

if x == y:
    z = x
elif x == 0 and y == 1:
    z = 2
elif x == 0 and y == 2:
    z = 1
elif x == 1 and y == 0:
    z = 2
elif x == 1 and y == 2:
    z = 0
elif x == 2 and y == 0:
    z = 1
elif x == 2 and y == 1:
    z = 0

print(z)
