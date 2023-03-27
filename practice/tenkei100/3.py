S = input()
N = len(S)


def ACGT(s):
    length = len(s)
    for i in range(length):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            pass
        else:
            return 0
    return length


ans = -10
for start in range(0, N+1):
    for end in range(start+1, N+1):
        ans = max(ans, ACGT(S[start:end]))

print(ans)
