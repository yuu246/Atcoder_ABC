graph = []
for i in range(4):
    x, y = map(int, input().split())
    graph.append([x, y])

for i in range(4):
    x1, y1 = graph[i]
    x2, y2 = graph[(i+1) % 4]
    x3, y3 = graph[(i+2) % 4]
    dx1, dy1 = x1 - x2, y1 - y2
    dx2, dy2 = x3 - x2, y3 - y2
    if dx1*dy2 - dx2*dy1 > 0:
        print('No')
        exit()

print('Yes')
