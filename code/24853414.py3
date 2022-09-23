n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    S = list(map(int, input().split()))
    N = [0 for i in range(a)]
    N[b] = 1
    cnt = 0
    while True:
        if S[0] == max(S):
            cnt += 1
            if N[0] == 1:
                print(cnt)
                break
            else:
                del S[0]
                del N[0]
        else:
            S.append(S[0])
            N.append(N[0])
            del S[0]
            del N[0]