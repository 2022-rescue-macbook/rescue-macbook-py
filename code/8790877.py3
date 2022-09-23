n=int(input());
for i in range(n):
    a=input().split();
    p=int(a[1])
    l=int(a[0])
    n=1;
    que=list(map(int,input().split(' ')));
    while(True):
        temp=que.pop(0);
        if(len(que)==0):
            print(l);
            break;
        if max(que)>temp:
            que.append(temp);
            p=(p-1)%len(que);
        else:
            if p==0:
                print(n);
                break;
            p=(p-1)%len(que);        
            n+=1;
        

