from collections import Counter
S = list(input())
N = len(S)
cnt = Counter(S)
flag = False

if N == 1:
    if S[0] == '8':
        flag = True
elif N == 2:
    for x in range(16, 104, 8):
        s_x = str(x)
        if s_x[0] == s_x[1]:
            if cnt[s_x[0]] >= 2:
                flag = True
                break
        else:
            if cnt[s_x[0]] >= 1 and cnt[s_x[1]] >= 1:
                flag = True
                break
else:
    for x in range(104, 1000, 8):
        s_x = str(x)
        if s_x[0] == s_x[1] == s_x[2]:
            if cnt[s_x[0]] >= 3:
                flag = True
                break
        elif s_x[0] == s_x[1]:
            if cnt[s_x[0]] >= 2 and cnt[s_x[2]] >= 1:
                flag = True
                break
        elif s_x[1] == s_x[2]:
            if cnt[s_x[1]] >= 2 and cnt[s_x[0]] >= 1:
                flag = True
                break
        elif s_x[0] == s_x[2]:
            if cnt[s_x[0]] >= 2 and cnt[s_x[1]] >= 1:
                flag = True
                break
        else:
            if cnt[s_x[0]] >= 1 and cnt[s_x[1]] >= 1 and cnt[s_x[2]] >= 1:
                flag = True
                break
if flag:
    print('Yes')
else:
    print('No')
