#!/usr/bin/env python3

graph = [
    [2, 3],
    [1, 4, 5],
    [1, 6, 7],
    [2, 8, 9],
    [2, 10, 11],
    [3, 12, 13],
    [3, 14, 15],
    [4],
    [4],
    [5],
    [5],
    [6],
    [6],
    [7],
    [7]
]
len(graph)
a, b = map(int, input().split())

if b in graph[a-1]:
    print('Yes')
else:
    print('No')
