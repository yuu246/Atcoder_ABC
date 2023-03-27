n, x = map(int, input().split())
A = list(map(int, input().split()))

ok = 0
ng = len(A)
while ng > ok:
    mid = (ok + ng) // 2
    if A[mid] > x:
        ng = mid
    elif A[mid] == x:
        print(mid+1)
        break
    else:
        ok = mid
