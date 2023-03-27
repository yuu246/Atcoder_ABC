N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = (N - 1)


while left <= right:
    mid = (left + right)//2
    if A[mid] == X:
        print(mid+1)
        break
    if A[mid] > X:
        right = mid - 1   
    if A[mid] < X:
        left = mid + 1