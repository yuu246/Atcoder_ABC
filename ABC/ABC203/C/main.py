#!/usr/bin/env python3
N, K = map(int, input().split())

friends = []
for _ in range(N):
    a, b = map(int, input().split())
    friends.append([a, b])

friends.sort()

now = 0
now += K
for i in range(N):
    friend = friends[i][0]
    money = friends[i][1]

    if friend <= now:
        now += money
    else:
        break
print(now)
