m = int(input())
base_x, base_y = map(int, input().split())
dif_map = set()
for _ in range(m-1):
    x, y = map(int, input().split())
    x, y = x - base_x, y - base_y
    dif_map.add((x, y))

n = int(input())
graph2 = []
for _ in range(n):
    x, y = map(int, input().split())
    graph2.append([x, y])

for i in range(n):
    tmp_dif_map = set()
    base2_x, base2_y = graph2[i]
    for j in range(n):
        if i == j:
            continue
        x, y = graph2[j]
        x, y = x - base2_x, y - base2_y
        tmp_dif_map.add((x, y))

    if dif_map.intersection(tmp_dif_map) == dif_map:
        ans_x = base2_x - base_x
        ans_y = base2_y - base_y
        print(f'{ans_x} {ans_y}')
        break
    else:
        continue
