import sys
I=sys.stdin.readline

def solve(a,m):
    cnt=1
    for i in range(9,a[m]-1,-1):
        while i in a:
            ind=a.index(i)
            if m==ind:return cnt
            a=a[ind+1:]+a[:ind]
            m=(m-ind-1)%(len(a)+1)
            cnt+=1
    return cnt

t=int(I())
for _ in range(t):
    n,m=map(int,I().split())
    *a,=map(int,I().split())
    print(solve(a,m))