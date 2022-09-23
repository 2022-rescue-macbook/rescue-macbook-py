n=int(input())
for _ in range(n):
    N,location=map(int,input().split())
    arr=list(map(int,input().split()))
    m=max(arr)
    count=0
    while 1:
        p=arr.pop(0)
        if p==m:
            if location==0:
                count+=1
                break
            else:
                location-=1
                count+=1
                m=max(arr)
        else:
            arr.append(p)
            if location==0:
                location=len(arr)-1
            else:
                location-=1
    print(count)