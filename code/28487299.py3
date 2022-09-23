num=int(input())
answer=[]
for i in range(0,num):
    n,m=input().split()
    n=int(n)
    m=int(m)
    array=list(map(int,input().split(" ")))
    num=0
    while(len(array)!=0):
        if array[0]==max(array):
            num+=1
            array.pop(0)
            
            if m!=0:
                m-=1
            else:
                break
        else:
            array.append(array.pop(0))
            if m!=0:
                m-=1
            else:
                m=len(array)-1
                
    answer.append(num) 

for each in answer:
    print(each)