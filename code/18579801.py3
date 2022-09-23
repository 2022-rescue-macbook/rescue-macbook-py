t=int(input())
result=[]
for i in range(t):
    paper,position=map(int,input().split())
    
    if paper==1:
        result.append(1)
        null=input()
        continue
    else:
        arr=input().split()
        arr=[int(j) for j in arr]
        count=0
        out=arr[0]
        m=max(arr[1:])

        while(True):
            if out>=m and position==0:
                count+=1
                result.append(count)
                break
            elif out>=m and position!=0:
                position-=1
                count+=1
                arr=arr[1:]
                out=arr[0]
                m=max(arr)
            elif out<m and position==0:
                position=len(arr)-1
                temp=arr[1:]
                arr=temp+[out]
                out=arr[0]
                m=max(arr[1:])
            else: #out<m abd position!=0:
                position-=1
                temp=arr[1:]
                arr=temp+[out]
                out=arr[0]
                m=max(arr[1:])
                
for i in range(t):
    print(result[i])

