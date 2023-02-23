ans = []
N = int(input())
while True:
    if N == 1:
        ans.append(1)
        break
    a = N % 2
    ans.append(a)
    N = N // 2


ans.reverse()
ans1 = map(str, ans)
str_ans = ''.join(ans1)
print(str_ans.zfill(10))
