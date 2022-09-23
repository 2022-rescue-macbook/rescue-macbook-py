num = int(input())
N,M,importances=[],[],[]
for _ in range(num):
    n, m = list(map(int, input().split()))
    importance = list(map(int, input().split()))
    N.append(n)
    M.append(m)
    importances.append(importance)

for i in range(num):
    n, m, importance = N[i], M[i], importances[i]
    count = 0

    while 1:
        most = max(importance)
        if importance[0] >= most:
            importance.pop(0)
            count += 1
            if m==0:
                break
        else:
            importance.append(importance.pop(0))
            if m==0:
                m=len(importance)-1
                continue
        m-=1

    print(count)