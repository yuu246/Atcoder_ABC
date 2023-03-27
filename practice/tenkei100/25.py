import sys
sys.setrecursionlimit(10**9)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 0indexにする
    graph = []
    for i in range(h):
        w_list = list(map(int, input().split()))
        graph.append(w_list)

    visited = []
    for i in range(h):
        visited.append([False] * w)

    def dfs(x, y):
        if not visited[x][y] and graph[x][y] == 1:
            visited[x][y] = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x2, y2 = x + dx, y + dy
                    if x2 < 0 or x2 >= h or y2 < 0 or y2 >= w:
                        continue
                    if graph[x2][y2] == 1:
                        dfs(x2, y2)

    ans = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and graph[y][x] == 1:
                ans += 1
                dfs(y, x)

    print(ans)
