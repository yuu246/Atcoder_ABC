N = int(input())
S = list(input())

cont = [[] for i in range(26)]
for i in range(N):
    num = ord(S[i]) - ord('a')
    cont[num].append(i)

j = 0
tail = N
for i in range(N):
    while j < 26:
        while cont[j] and (cont[j][-1] > tail or cont[j][-1] <= i):
            cont[j].pop()
        if not cont[j]:
            j += 1
        else:
            break
    if tail <= i:
        break
    if ord(S[i])-ord('a') > j:
        S[i], S[cont[j][-1]] = S[cont[j][-1]], S[i]
        tail = cont[j][-1]
        cont[j].pop()
print(''.join(S))
