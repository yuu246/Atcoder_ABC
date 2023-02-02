#!/usr/bin/env python3
S = list(input())

length = len(S)
ans = 0

for i in range(length):
    if S[i] == 'A':
        x = 1
    if S[i] == 'B':
        x = 2
    if S[i] == 'C':
        x = 3
    if S[i] == 'D':
        x = 4
    if S[i] == 'E':
        x = 5
    if S[i] == 'F':
        x = 6
    if S[i] == 'G':
        x = 7
    if S[i] == 'H':
        x = 8
    if S[i] == 'I':
        x = 9
    if S[i] == 'J':
        x = 10
    if S[i] == 'K':
        x = 11
    if S[i] == 'L':
        x = 12
    if S[i] == 'M':
        x = 13
    if S[i] == 'N':
        x = 14
    if S[i] == 'O':
        x = 15
    if S[i] == 'P':
        x = 16
    if S[i] == 'Q':
        x = 17
    if S[i] == 'R':
        x = 18
    if S[i] == 'S':
        x = 19
    if S[i] == 'T':
        x = 20
    if S[i] == 'U':
        x = 21
    if S[i] == 'V':
        x = 22
    if S[i] == 'W':
        x = 23
    if S[i] == 'X':
        x = 24
    if S[i] == 'Y':
        x = 25
    if S[i] == 'Z':
        x = 26
    ans += x * 26**(length-i-1)

print(ans)