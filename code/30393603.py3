import sys
t=int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    joo=list(map(int,sys.stdin.readline().split()))
    standard=list(range(n))
    standard[m]='t'
    count=0
    i=0
    while True:
        if max(joo)==joo[i]:
            count+=1
            if standard[0]=='t':
                print(count)
                break
            else:
                del joo[0]
                del standard[0]
        else:
            joo.append(joo.pop(0))
            standard.append(standard.pop(0))