import sys

T = int(sys.stdin.readline())
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    l = list(enumerate(map(int, sys.stdin.readline().split())))
    cnt = 0
    while True:
        k = l.index(max(l,key=lambda x : x[1]))
        cnt +=1
        if l[k][0]==m : break
        if k==0 : l = l[1:]
        elif k==len(l)-1 : del l[-1]
        else : l = l[k+1:] + l[:k]
    print(cnt)