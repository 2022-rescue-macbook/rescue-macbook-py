import sys
input=sys.stdin.readline

n=int(input())

def loca(lst, n):
    for i in range(len(lst)-1,-1,-1):
        if lst[i]==n:
            return i
    return -1

for i in range(n):
    m, idx=map(int, input().split())
    lst=list(map(int, input().split()))
    std=lst[idx]
    cnt=0

    lst[idx]=[lst[idx]]
    for i in range(9, std, -1):
        newlst=[]
        loc=loca(lst, i)
        for j in range(loc+1):
            if isinstance(lst[j], list):
                newlst.append(lst[j])
                continue
            if lst[j]==i:
                cnt+=1
            else:
                newlst.append(lst[j])
        newlst=lst[loc+1:]+newlst
        lst=newlst
    for i in lst:
        if isinstance(i, list):
            cnt+=1
            break
        else:
            if i==std:
                cnt+=1
    print(cnt)
