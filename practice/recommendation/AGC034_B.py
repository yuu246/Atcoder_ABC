s = input()
s = s.replace('BC', 'X')

ans = 0
A = 0
for i in range(len(s)):
    if s[i] == 'A':
        A += 1
    elif s[i] == 'X':
        ans += A
    else:
        A = 0
print(ans)
