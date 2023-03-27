import bisect
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.sort()
length = len(A_list)
sum_A = [0 for i in range(N+1)]
for i in range(1, N+1):
    sum_A[i] = sum_A[i-1] + A_list[i-1]

for _ in range(Q):
    x = int(input())
    idx = bisect.bisect(A_list, x)
    if idx == 0:
        ans = sum_A[N] - x * length
    if 1 <= idx <= length:
        ans = x * idx - sum_A[idx] + (sum_A[N] - sum_A[idx]) - x * (N-idx)
    if idx == length + 1:
        ans = x * length - sum_A[N]

    print(ans)
