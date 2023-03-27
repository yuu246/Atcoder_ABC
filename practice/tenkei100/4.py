N, M = map(int, input().split())
A_list = [[]]
for i in range(N):
    a = [0] + list(map(int, input().split()))
    A_list.append(a)

ans = 0

for i in range(1, M):
    for j in range(i+1, M+1):
        tmp = 0
        for k in range(1, N+1):
            tmp += max(A_list[k][i], A_list[k][j])
        ans = max(ans, tmp)

print(ans)
