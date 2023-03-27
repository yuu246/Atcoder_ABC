D = int(input())
N = int(input())

menber = [0]*(D+2)

for i in range(N):
    L, R = map(int, input().split())
    menber[L] += 1
    menber[R+1] -= 1

ans = [0]*(D+2)
for i in range(1, D+1):
    ans[i] = ans[i-1] + menber[i]

for i in range(1, D+1):
    print(ans[i])
