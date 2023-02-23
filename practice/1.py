N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))


def check(x: int, y: int):
    ok = 1
    ng = N
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if A[mid] <= y+K:
            ok = mid
        else:
            ng = mid
    if A[ng] < y + K:
        return (ng - x)
    return (ok - x)


ans = 0
for i in range(1, N+1):
    ans += check(i, A[i])

print(ans)
