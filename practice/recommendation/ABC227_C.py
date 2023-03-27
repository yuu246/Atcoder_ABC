N = int(input())

keta1 = 0
keta2 = 0
ans = 0
while True:
    keta2 = keta1
    keta1 += 1
    if N // (keta1*keta1) < (keta1):
        break
    while True:
        keta2 += 1
        if N // (keta2*keta1) >= keta2:
            ans += (N // (keta2*keta1)) - keta2 + 1
        else:
            break

print(ans)
