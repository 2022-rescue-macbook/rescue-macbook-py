for i in range(int(input())):
    count=0
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    while 1:
        if arr[0]==max(arr):
            count+=1
            if m==0:
                print(count)
                break
            arr.pop(0)
            m-=1
        else:
            arr.append(arr.pop(0))
            if m==0:
                m=len(arr)-1
            else:
                m-=1