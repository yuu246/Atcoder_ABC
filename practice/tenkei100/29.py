from collections import deque
R, C = map(int, input().split())

sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
graph = [[]]
for i in range(R):
    gyou = [0] + list(input())
    graph.append(gyou)

Q = deque()
Q.append([sy, sx])
counter = [[-1 for _ in range(C+1)] for i in range(R)]
counter[sy][sx] = 0
while len(Q) > 0:
    y, x = Q.popleft()
    for y2, x2 in [[y-1, x], [y, x-1], [y, x+1], [y+1, x]]:
        if graph[y2][x2] == '.' and counter[y2][x2] == -1:
            Q.append([y2, x2])
            counter[y2][x2] = counter[y][x] + 1

print(counter[gy][gx])
