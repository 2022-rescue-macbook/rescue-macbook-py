###### ### input case 
C = int(input())
NM = [[]] * C
N = [0] * C
M = [0] * C
imp_s = [0] * C
imp_i = [[]] * C
cnt = [0] * C
judge = [[]] * C
for i in range(C):
    NM[i] = list(input().split(' '))
    N[i] = int(NM[i][0]) ##  총 문서의 갯수 각 case 당 
    M[i] = int(NM[i][-1]) ###  알고자 하는 문서의 위치 
    imp_s[i] = list(input().split(' '))
    imp_i[i] = [0] * len(imp_s[i])
    judge[i] = [0] * N[i]
    judge[i][M[i]] = 'T'
    for j in range(len(imp_s[i])):
        imp_i[i][j] = int(imp_s[i][j]) ## 중요도를 리스트로 

    ##f len(imp_i[i]) == N[i]:
    while True:
        if imp_i[i][0] == max(imp_i[i]):
            cnt[i] += 1
            if judge[i][0] == 'T':
                print(cnt[i])
                break
            else:
                imp_i[i].pop(0)
                judge[i].pop(0)
        else:
            imp_i[i].append(imp_i[i].pop(0))
            judge[i].append(judge[i].pop(0))
