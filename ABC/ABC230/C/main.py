#!/usr/bin/env python3
# from collections import deque

# N, A, B = map(int, input().split())
# P, Q, R, S = map(int, input().split())
# ans_list = deque()


# def task1():
#     left = max(1-A, 1-B)
#     right = min(N-A, N-B)
#     if left + B < R or left+A < P:
#         left = max(R - B, P - A)
#     if right + B > S or right + A > Q:
#         right = min(S-B, Q-A)
#     for k in range(left, right+1):
#         y = A+k
#         x = B+k
#         if R <= x <= S and P <= y <= Q:
#             ans_list.append([y-P, x-R])


# def task2():
#     left = max(1-A, B-N)
#     right = min(N-A, B-1)
#     if B - left < R or left+A < P:
#         left = max(B - R, P - A)
#     if B - right > S or right + A > Q:
#         right = min(B-S, Q-A)
#     for k in range(left, right+1):
#         y = A+k
#         x = B-k
#         if R <= x <= S and P <= y <= Q:
#             ans_list.append([y-P, x-R])


# task1()
# task2()
# ans = []
# for i in range(Q-P+1):
#     tmp = ['.'] * (S-R+1)
#     ans.append(tmp)

# for y, x in ans_list:
#     ans[y][x] = '#'

# for i in range(Q-P+1):
#     tmp = ans[i]
#     ans1 = ''.join(tmp)
#     print(ans1)


N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

H = Q - P + 1
W = S - R + 1

for i in range(P, Q + 1):
    ans = []  # 文字列の連結が遅いPyPyでは、文字列を+=で連結するとTLEになります
    for j in range(R, S + 1):
        if (i - j == A - B) or (i + j == A + B):
            ans.append("#")
        else:
            ans.append(".")
    print(*ans, sep="")
