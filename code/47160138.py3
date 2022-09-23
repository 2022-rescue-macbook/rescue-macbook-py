import sys
input=sys.stdin.readline

k=int(input())
for i in range(k):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    data_q=[[j,l] for j,l in enumerate(data)]
    data.sort(reverse=True)
    j=0
    cnt=1
    while True:
        while data_q[0][1]!=data[j]:
            data_q.append(data_q[0])
            del data_q[0]
        j+=1
        if data_q[0][0]==m:
            print(cnt)
            break
        del data_q[0]
        cnt+=1