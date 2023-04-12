N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    a = list(input())
    A.append(a)
for j in range(M):
    b = list(input())
    B.append(b)


def check(si, sj):
    for i in range(M):
        for j in range(M):
            if A[si+i][sj+j] != B[i][j]:
                return False
    return True


for si in range(N-M+1):
    for sj in range(N-M+1):
        if check(si, sj):
            print('Yes')
            exit()

print('No')
