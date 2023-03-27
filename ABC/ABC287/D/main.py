#!/usr/bin/env python3

S = input()
T = input()

# length = len(T)
# for x in range(length + 1):
#     if x == 0:
#         S_dash = S[-length:]
#     elif x == length:
#         S_dash = S[:x]
#     else:
#         S_dash = S[:x] + S[-(length -x):]

#     flag = True
#     for i in range(length):
#         if S_dash[i] == '?' or T[i] =='?':
#             continue
#         if S_dash[i] != T[i]:
#             flag = False
#             break
#     if flag:
#         print('Yes')
#     else:
#         print('No')

def match_or_not(a, b):
    if a == b or a == '?' or b== '?':
        return True
    else:
        return False

pre = [False] * (len(T) + 1)
suf = [False] * (len(T) + 1)

pre[0] = True
for i in range(len(T)):
    if not match_or_not(T[i], S[i]):  # 一致しなかったらそれ以降すべてマッチせず
        break
    else:
        pre[i + 1] = True
s = S[::-1]
t = T[::-1]

suf[0] = True

for i in range(len(t)):
    if not match_or_not(t[i], s[i]):
        break
    else:
        suf[i + 1] = True

for i in range(len(t) + 1):
    if pre[i] and suf[len(t) - i]:
        print("Yes")
    else:
        print("No")

