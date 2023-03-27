#!/usr/bin/env python3

from itertools import product
import math
N, X = map(int, input().split())

hukuro = [list(map(int, input().split()))[1:] for i in range(N)]


ans = 0
for com in product(*hukuro):
    if math.prod(com) == X:
        ans += 1

print(ans)

# from itertools import product
# N, X = map(int, input().split())
# ans = 0

# balls = []
# for _ in range(N):
#     ball = list(map(int, input().split()))
#     balls.append(ball[1:])

# for x in product(*balls):
#     kumiawase = list(x)
#     tmp = 1
#     for y in kumiawase:
#         tmp = tmp * y
#     if tmp == X:
#         ans += 1
# print(ans)
