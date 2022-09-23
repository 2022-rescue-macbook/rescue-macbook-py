t = int(input())
for q in range(t):
    n,m = map(int,input().split())
    quimp = list(map(int,input().split()))
    qun = [x for x in range(n)]
    cnt = 1
    for i in range(n):
        maxa = max(quimp)
        maxap = -1
        l = len(quimp)
        for j in range(len(quimp)):
            if maxa == quimp[j]:
                maxap = j
                break
        if qun[maxap] == m:
            break
        quimp = quimp[min(l,maxap+1):] + quimp[:maxap]
        qun = qun[min(l,maxap+1):] + qun[:maxap]
        cnt += 1
    print(cnt)