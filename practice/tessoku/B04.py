N = input()
ans = 0
length = len(N)

for i in range(0, length):
    ans += int(N[i])*(2**(length-i-1))

print(ans)
