#!/usr/bin/env python3

S = input()
a, b = map(int, input().split())
a -= 1
b -= 1
ans = S[:a] + S[b:b+1] + S[a+1:b] + S[a:a+1] + S[b+1:]
print(ans)
