N = int(input())


def check(n):
    if n % 2 == 1:
        ans = 0
        yaku = int(n ** 0.5)
        for i in range(1, yaku+1):
            if n % i == 0:
                ans += 2
            if i * i == n:
                ans -= 1
        if ans == 8:
            return True
        else:
            return False


answer = 0
for n in range(1, N+1):
    if check(n):
        answer += 1

print(answer)
