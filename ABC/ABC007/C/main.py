#!/usr/bin/env python3


from collections import deque

R, C = map(int, input().split())

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

gx, gy = map(int, input().split())
gx -= 1
gy -= 1

graph = []
for _ in range(R):
    c = list(input())
    graph.append(c)

dist = []
for _ in range(R):
    dist.append([-1] * C)

Q = deque()
Q.append([sx, sy])
dist[sx][sy] = 0

while len(Q) > 0:
    x, y = Q.popleft()

    for x2, y2 in [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]:

        if not ( 0 <= x2 < R and 0 <= y2 < C):
            continue

        if graph[x][y] == '#':
            continue

        if graph[x2][y2] == '.' and dist[x2][y2] == -1:
            dist[x2][y2] = dist[x][y] + 1
            Q.append([x2, y2])
   

print(dist[gx][gy])