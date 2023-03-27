import sys
sys.setrecursionlimit(10**9)
N = int(input())
ans = list()
graph = [list() for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(N+1):
    graph[i].sort()


def dfs(now, pre):
    ans.append(now)
    for next in graph[now]:
        if next != pre:
            dfs(next, now)
            ans.append(now)


dfs(1, -1)
print(*ans)
