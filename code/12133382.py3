from sys import stdin as st
N=eval(st.readline())

for z in range(N):
    a, b= map(eval, st.readline().split())
    x=list(map(eval,st.readline().split()))
    c=[]
    for j in x:
        c.append(j)
    l=1
    while True:
        if b==0:
            if max(c)==c[0]:
                c.pop(0)
                print(l)
                break
            else:
                b=len(c)-1
                c.append(c.pop(0))
        else:
            if max(c)==c[0]:
                c.pop(0)
                l+=1
                b-=1
            else:
                c.append(c.pop(0))
                b-=1