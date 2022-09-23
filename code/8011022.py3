N = int(input())

def numfinder(N):
    return N[0]

for x in range(N):
    ans = 1 #출력할 답
    ipt = [int(i) for i in input().split()] # N과 M 입력받기
    num = ipt[0]
    q = [[int(i),False] for i in input().split()]
    q[ipt[1]][1] = True
    maxnum = max(q, key=numfinder)[0]
    while 1:
        if q[0][0] == maxnum:
            if q[0][1] == True:
                break
            else:
                q.pop(0)
                ans += 1
                maxnum = max(q, key=numfinder)[0]
        else:
            q.append(q.pop(0))
    print(ans)