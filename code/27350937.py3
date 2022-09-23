case_num=int(input())

for i in range(case_num):
    n,m=map(int,input().split())
    w =list(map(int,input().split()))
    result=0
    cur_pos=m
    while(len(w)!=0):
        max_val=max(w)
        while(w[0]!=max_val):
            if(cur_pos==0):
                cur_pos=len(w)
            cur_pos-=1
            a = w.pop(0)
            w.append(a)
        w.pop(0)
        result+=1
        if cur_pos==0:
            print(result)
            break
        cur_pos-=1
