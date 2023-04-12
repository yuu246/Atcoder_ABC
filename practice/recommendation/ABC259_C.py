S = input()
T = input()


def rls(S):
    n = len(S)
    ans = []
    l = 0
    while l < n:
        r = l+1
        while r < n and S[l] == S[r]:
            r += 1
        ans.append((S[l], r-l))
        l = r
    return ans


S_list = rls(S)
T_list = rls(T)
flag = False

if len(S_list) != len(T_list):
    print('No')
    exit()
for i in range(len(S_list)):
    s, x = S_list[i]
    t, y = T_list[i]
    if s != t:
        flag = False
        break
    if x == 1 and y > 1:
        flag = False
        break
    if 2 <= x and y < x:
        flag = False
        break
else:
    flag = True
if flag:
    print('Yes')
else:
    print('No')

