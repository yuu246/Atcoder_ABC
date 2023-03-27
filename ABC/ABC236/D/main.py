#!/usr/bin/env python3


N = int(input())

scores = [[]]
for i in range(2*N-1):
    score = [-1] + list(map(int, input().split()))
    scores.append(score)


dancer = [i for i in range(1, 2*N+1)]
ans = 0


def calc(dancer, score):
    if len(dancer) == 0:
        global ans
        ans = max(ans, score)
        return
    man = dancer[0]
    for i in range(1, len(dancer)):
        woman = dancer[i]
        calc(dancer[1:i] + dancer[i+1:], score ^ scores[man][woman-man])


calc(dancer, 0)
print(ans)
