t = int(input())
s1=[]
for i in range(t):
    s1 = []
    idx =0
    c = 0
    n,m= map(int,input().split())
    a= list(map(int,input().split()))
    for p,q in enumerate(a):
        s1.append([q,p+1])
    s1[m][1] = 0
    
    while a:
        if idx > len(a)-1:
            idx = idx%len(a)
        e = max(a)
        
        if s1[idx][0]==e:
            if s1[idx][1] == 0:
                print(c+1)
                break
            s1.pop(idx)
            a.pop(idx)
            c +=1
        elif s1[idx][0]<e:
            idx+=1