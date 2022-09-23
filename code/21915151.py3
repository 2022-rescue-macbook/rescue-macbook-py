def print_q(n,m):
    queue =input().split()
    a=1
    b=m
    c=queue[m]
    while True:
        if queue[0]== max(queue)and (queue[0] != c or b !=0):
            del queue[0]
            a=a+1
            b=b-1
            
        elif b==0 and queue[b]== max(queue):
            print(a)
            break
        else:
            queue.append(queue[0])
            del queue[0]  
            b=b-1

            if b==-1:
                b=n-a


number=int(input())
i=0
for i in range(number):
    x=input().split()
    m=map(int,x)
    num,indexnum =m
    print_q(num,indexnum)