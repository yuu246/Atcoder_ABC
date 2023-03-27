#!/usr/bin/env python3

S = input()
str_list = list(reversed(S))
r_S = ''.join(str_list)
r_S = r_S.replace('6', 'a')
r_S = r_S.replace('9', '6')
r_S = r_S.replace('a', '9')

print(r_S)
