T=int(input())
for t in range(T):
    N,idx=map(int,input().split())    
    li=(list(map(int, input().split(' '))))
    ans=0
    check=[0]*N
    check[idx]='T'
    if N==1:
        print(1)
        continue
    if len(list(set(li)))==1:
        print(idx+1)
        continue
    while True:
        #print(li,check)
        if li[0]==max(li): ##가장 큰 수 일때
            ans=ans+1
            if check[0]=='T':
                print(ans)
                break
            else:
                li.pop(0)
                check.pop(0)
        else: ##아직 큰 수가 남아있을때
            li.append(li.pop(0))
            check.append(check.pop(0))

    