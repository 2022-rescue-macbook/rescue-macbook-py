T = int(input())
for t in range(T):
    N,M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    count = 0
    p = 0
    while True:
        i = 0
        for i in range(len(A)):
            if A[i]==max(A):
                if i==M:
                    print(count+1)
                    p = 1
                    break
                else:
                    A[i]=0
                    count += 1
        if p==1:
            break