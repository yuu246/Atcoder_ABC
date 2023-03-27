#!/usr/bin/env python3

H, W = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(H)]
art = [list() for i in range(H)]
alpa = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(H):
    tmp = ''
    for j in graph[i]:
        if j == 0:
            tmp += '.'
        else:
            tmp += alpa[j].upper()
    art[i].append(tmp)

for i in range(H):
    print(*art[i])
