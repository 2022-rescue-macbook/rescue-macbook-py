import sys
for _ in range(int(input())):
    N,M=map(int,input().split())
    a=list(map(int,input().split()))
    chul=1
    while True :
        #print(a, M)
        if a[0] == max(a):
            if M==0:
                print(chul)
                break
            else:
                a.pop(0)
                chul+=1
                M-=1
        else :
            a.append(a.pop(0))
            if M==0:
                M=len(a)-1
            else :
                M-=1