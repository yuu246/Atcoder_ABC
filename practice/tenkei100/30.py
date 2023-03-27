from collections import deque
H, W, N = map(int, input().split())

graph = [[]]
for _ in range(H):
    gyou = [0] + list(input())
    graph.append(gyou)


power = 1
timer = 0

for y in range(1, H+1):
    for x in range(1, W+1):
        if graph[y][x] == 'S':
            sy = y
            sx = x

graph[sy][sx] = '.'


def bfs(sy, sx, timer, power):
    Q = deque()
    counter = [[-1 for i in range(W+1)] for j in range(H+1)]
    Q.append([sy, sx])
    counter[sy][sx] = timer
    while len(Q) > 0:
        y, x = Q.popleft()
        for y2, x2 in [[y-1, x], [y, x-1], [y, x+1], [y+1, x]]:
            if 1 <= y2 <= H and 1 <= x2 <= W and graph[y2][x2] != 'X' and counter[y2][x2] == -1:
                Q.append([y2, x2])
                counter[y2][x2] = counter[y][x] + 1
                if graph[y2][x2] == str(power):
                    power += 1
                    return [y2, x2, counter[y2][x2], power]


for i in range(1, N+1):
    sy, sx, timer, power = bfs(sy, sx, timer, power)

print(timer)
