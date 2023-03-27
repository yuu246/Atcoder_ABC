#!/usr/bin/env python3

def binary_serch(x):
    ok = 0
    ng = len(seito)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if seito[mid] < x:
            ok = mid
        else:
            ng = mid
    return len(seito) - ok - 2


N, Q = map(int, input().split())
seito = [0] + list(map(int, input().split())) + [10**10]
seito.sort()

for i in range(Q):
    x = int(input())
    print(binary_serch(x))
