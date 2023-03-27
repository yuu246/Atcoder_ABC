N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(X, N, K, A:list):
    sum = 0
    for i in range(N):
        sum += X // A[i]
    if sum >= K:
        return True
    return False

left = 1
right = 10 ** 9
while left < right:
    mid = (left + right) // 2
    ans = check(mid, N, K, A)

    if ans == False:
        left = mid + 1
    if ans:
        right = mid

print(left)