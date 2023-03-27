#!/usr/bin/env python3

N, K = map(int, input().split())
P_list = [0] + list(map(int, input().split()))

ans = []
tmp_K = K
for i in range(N, K-1, -1):
    if P_list[i] > tmp_K:
        ans.append(tmp_K)
    elif P_list[i] <= tmp_K:
        tmp_K -= 1
        ans.append(tmp_K)

ans.reverse()

print(ans)
