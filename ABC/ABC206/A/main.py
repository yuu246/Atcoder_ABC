#!/usr/bin/env python3

N = int(input())
if int(1.08 * N) < 206:
    print('Yay!')
elif int(1.08 * N) == 206:
    print('so-so')
else:
    print(':(')
