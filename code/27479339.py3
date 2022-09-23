

N=int(input())

def get_topp(li):
    ret=1
    for a in range(1,10):
        if(li[a]>0):
            ret=a
    return ret

for _ in range(N):
    a=[int(i) for i in input().split(" ")]
    n, t=a[0], a[1]
    li=[int(i) for i in input().split(" ")]

    pri=[0]*10
    target_pri=li[t]

    for e in li:
        pri[e]+=1

    ans=1

    while(True):
        cur_pri=get_topp(pri)
        if(t==0):
            if(cur_pri==target_pri):
                print(ans)
                break
            else:
                a=li.pop(0)
                li.append(a)
                t=n-1
        else:
            a=li.pop(0)
            if(cur_pri==a):
                n-=1
                ans+=1
                pri[a]-=1
            else:
                li.append(a)
            t-=1
                
            


        
