#!/usr/bin/env python3

from collections import deque

a, N = map(int, input().split())

Q = deque()

q = deque()

MAX_N = 10 ** 6

dist = [-1] * MAX_N

dist[1] = 0
