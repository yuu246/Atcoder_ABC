from collections import defaultdict
from itertools import combinations
N = int(input())
dct = defaultdict(int)
for _ in range(N):
    s = input()
    if s[0] == 'M':
        dct['M'] += 1
    elif s[0] == 'A':
        dct['A'] += 1
    elif s[0] == 'R':
        dct['R'] += 1
    elif s[0] == 'C':
        dct['C'] += 1
    elif s[0] == 'H':
        dct['H'] += 1
    else:
        continue
ans = 0
for comb in combinations(['M', 'A', 'R', 'C', 'H'], 3):
    tmp = 1
    tmp *= dct[comb[0]]
    tmp *= dct[comb[1]]
    tmp *= dct[comb[2]]
    ans += tmp
print(ans)
