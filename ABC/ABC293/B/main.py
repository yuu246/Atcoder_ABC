#!/usr/bin/env python3
N = int(input())
flag_list = [False for i in range(N+1)]
yobare = set()
all_hito = set([i for i in range(1, N+1)])
hito = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    if not flag_list[i]:
        flag_list[hito[i]] = True
        yobare.add(hito[i])

ans = all_hito.difference(yobare)
ans = list(ans)
print(len(ans))
print(*ans)
