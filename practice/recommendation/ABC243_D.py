from collections import deque
N, X = map(int, input().split())

S = list(input())
Q = deque()
cont = 0
for moji in S:
    if moji == 'U':
        if len(Q) > 0:
            Q.pop()
        else:
            cont += 1
    elif moji == 'R':
        Q.append('R')
    elif moji == 'L':
        Q.append('L')

for i in range(cont):
    X //= 2
for moji in Q:
    if moji == 'R':
        X *= 2
        X += 1
    else:
        X *= 2

print(X)
