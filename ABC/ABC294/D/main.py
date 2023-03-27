#!/usr/bin/env python3
from sys import stdin
import heapq
N, Q = map(int, input().split())

hito = 1

called = []
rec = set()

for i in range(Q):
    event = list(map(int, stdin.readline().split()))

    if event[0] == 1:
        heapq.heappush(called, hito)
        hito += 1

    elif event[0] == 2:
        x = event[1]
        rec.add(x)

    else:
        while True:
            x = heapq.heappop(called)
            if x in rec:
                continue
            else:
                print(x)
                break
        heapq.heappush(called, x)
