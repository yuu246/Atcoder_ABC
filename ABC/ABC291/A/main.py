N = int(input())
X_list = list(map(int, input().split()))
X_list.sort()
sum_list = X_list[N:4*N]
ans = sum(sum_list) / (3*N)
print(ans)
