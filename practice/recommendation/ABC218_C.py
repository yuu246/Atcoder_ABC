N = int(input())

S = []
for i in range(N):
    s = list(input())
    S.append(s)

T = []
for i in range(N):
    t = list(input())
    T.append(t)

cntS = sum(1 for i in range(N) for j in range(N) if S[i][j] == '#')
cntT = sum(1 for i in range(N) for j in range(N) if T[i][j] == '#')
if cntS != cntT:
    print('No')
    exit()


T_90 = list(zip(*T[::-1]))


T_270 = list(zip(*T))
T_270 = T_270[::-1]

T_180 = []
for i in range(len(T)):
    T_180.append(T[i][::-1])
T_180 = T_180[::-1]


def find(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                return i, j


def shapes(S, T):
    sx, sy = find(S)
    tx, ty = find(T)
    dif_x = sx - tx
    dif_y = sy - ty
    new_T = [['.' for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i - dif_x < 0 or i - dif_x > N-1:
                new_T[i][j] = '.'
            elif j - dif_y < 0 or j - dif_y > N-1:
                new_T[i][j] = '.'
            else:
                new_T[i][j] = T[i-dif_x][j-dif_y]
    if S == new_T:
        return True
    else:
        return False


flag = False
if shapes(S, T):
    flag = True
if shapes(S, T_90):
    flag = True
if shapes(S, T_180):
    flag = True
if shapes(S, T_270):
    flag = True

if flag:
    print('Yes')
else:
    print('No')
