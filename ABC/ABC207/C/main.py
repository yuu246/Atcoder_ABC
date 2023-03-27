#!/usr/bin/env python3

def change(kukan_list):
    t = kukan_list[0]
    if t == 1:
        return kukan_list[1], kukan_list[2]
    if t == 2:
        return kukan_list[1], kukan_list[2] - 0.5
    if t == 3:
        return kukan_list[1] + 0.5, kukan_list[2]
    if t == 4:
        return kukan_list[1] + 0.5, kukan_list[2] - 0.5


def judge(list1, list2):
    l1, r1 = change(list1)
    l2, r2 = change(list2)
    if max(l1, l2) <= min(r1, r2):
        return True


N = int(input())
all_list = []
for i in range(N):
    kukan = list(map(int, input().split()))
    all_list.append(kukan)

ans = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if judge(all_list[i], all_list[j]):
            ans += 1

print(int(ans/2))
