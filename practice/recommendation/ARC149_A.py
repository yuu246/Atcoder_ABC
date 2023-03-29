N, M = map(int, input().split())
mx = [0, 0]
for i in range(1, 10):
    tmp = 0
    for j in range(1, N+1):
        tmp = tmp*10 + i
        tmp %= M
        if tmp == 0:
            mx = max(mx, [j, i])

if mx[0] != 0:
    print(str(mx[1])*mx[0])
else:
    print(-1)
