from itertools import permutations

N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))
ans = []
idx = 0
for arr in permutations([i for i in range(1, N+1)]):
    arr = list(arr)
    idx += 1
    if arr == p_list:
        ans.append(idx)
    if arr == q_list:
        ans.append(idx)

answer = abs(ans[0] - ans[1])
print(answer)
