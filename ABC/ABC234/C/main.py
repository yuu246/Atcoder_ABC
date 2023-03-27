#!/usr/bin/env python3
from collections import deque
K = int(input())


def change(x):
    tmp = deque()
    if x == 1:
        tmp.append(1)
        return tmp
    else:
        while True:
            tmp.append(x % 2)
            x = x // 2
            if x == 1:
                tmp.append(x)
                break
        return tmp


ans_2 = change(K)
ans = ''
while len(ans_2) > 0:
    i = ans_2.pop()
    if i == 1:
        ans += '2'
    else:
        ans += '0'

print(ans)
