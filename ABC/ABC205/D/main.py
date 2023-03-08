#!/usr/bin/env python3

N, Q = map(int, input().split())
A_list = [0] + list(map(int, input().split())) + [10**18 + 1]

A_list.sort()


def binary_serch(x):
    ok = 0
    ng = N + 1

    while abs(ng) - abs(ok) > 1:
        mid = (ok + ng) // 2
        if A_list[mid] < x:
            ok = mid
        if A_list[mid] == x:
            return mid
        if A_list[mid] > x:
            ng = mid
    return ok


for i in range(Q):
    K = int(input())
    ans = K
    before = 0
    while True:
        now = binary_serch(ans)
        ans += now - before
        next = binary_serch(ans)
        if next == now:
            break
        else:
            before = now
    print(ans)
