test = int(input())
result = []

for i in range(test):
    fir_in = 0
    count = 0
    n, m = list(map(int, input().split()))
    que = list(map(int, input().split()))
    while True:
        if(que[fir_in]==max(que)):
            if(fir_in==m):
                result.append(count+1)
                break
            else:
                que[fir_in] = 0
                count += 1
        else:
            fir_in += 1
            fir_in = fir_in%n

for i in result:
    print(i)