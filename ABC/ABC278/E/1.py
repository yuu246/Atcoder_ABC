bingo = list()
for i in range(3):
    A = list(map(int, input().split()))
    bingo.append(A)
N = int(input())
ans = [[False]*3 for i in range(3)]

for i in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == b:
                ans[i][j] = True

flag = False
for i in range(3):
    if sum(ans[i]) == 3:
        flag = True
for i in range(3):
    if ans[0][i] + ans[1][i] + ans[2][i] == 3:
        flag = True

if ans[0][0] + ans[1][1] + ans[2][2] == 3:
    flag = True
if ans[2][0] + ans[1][1] + ans[0][2] == 3:
    flag = True

if flag:
    print('Yes')
else:
    print('No')
