#!/usr/bin/env python3
import math


def make_divisors(n):
    i = 2
    while True:
        if n % i == 0:
            p = i
            if i != n // i:
                q = n//i
                break
        i += 1
    return p, q


T = int(input())
for i in range(T):
    N = int(input())
    x, y = make_divisors(N)
    if y % x == 0:
        p = x
        q = y // x
    else:
        p = int(math.sqrt(y))
        q = x
    print(f'{p} {q}')
