S = '?' + input()

K = int(input())
N = len(S)
sum = [0 for i in range(N)]

for i in range(1, N):
    if S[i] == '.':
        sum[i] = sum[i-1] + 1
    else:
        sum[i] = sum[i-1]

ans = 0

right = 1
for left in range(1, N):
    while right < N:
        number_p = sum[right] - sum[left-1]
        if number_p <= K:
            right += 1
        else:
            break
    ans = max(ans, right - left)

print(ans)
