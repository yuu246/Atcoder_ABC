#!/usr/bin/env python3

T = 'oxx' * 10
S = input()

length = len(T)
s_length = len(S)
for i in range(length-s_length):
    if T[i:i+s_length] == S:
        print('Yes')
        break
else:
    print('No')
