#!/usr/bin/env python3

A, B, C, D = map(int, input().split())

if B / C < D:
    blue = A
    red = 0
    counter = 0

    while True:
        blue += B
        red += C
        counter += 1
        tmp = blue / red
        if tmp <= D:
            print(counter)
            break
else:
    print(-1)
