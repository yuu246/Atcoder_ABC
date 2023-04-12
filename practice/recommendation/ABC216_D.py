N, M = map(int, input().split())
T = []
for i in range(M):
    k = int(input())
    T.append(list(map(int, input().split())))

Now = [0] * (N+1)

for i in range(M):
    t = T[i][0]
    Now[t] += 1

Next = [[] for i in range(N+1)]

for i in range(M):
    for j in range(len(T[i]) - 1):
        Next[T[i][j]].append(T[i][j+1])

Q = []

for i in range(N+1):
    if Now[i] == 2:
        Q.append(i)

while Q:
    x = Q.pop()
    Now[x] = 0
    for to in Next[x]:
        Now[to] += 1
        if Now[to] == 2:
            Q.append(to)

if max(Now) == 0:
    print('Yes')
else:
    print('No')
