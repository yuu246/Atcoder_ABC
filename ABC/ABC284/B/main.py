#!/usr/bin/env python3
def odd(N, test):
    tmp = 0
    for i in range(N):
        if test[i] % 2 == 1:
            tmp += 1
    return tmp


T = int(input())

for i in range(T):
    N = int(input())
    test = list(map(int, input().split()))
    print(odd(N, test))
