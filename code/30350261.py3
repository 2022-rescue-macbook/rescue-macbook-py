import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    i=0
    while(len(importance)):
        if(importance[0] == max(importance)):
            importance = importance[1:]
            i += 1
            if(m==0):
                print(i)
                break
            m -= 1
        else:
            importance.append(importance[0])
            importance = importance[1:]
            if(m==0):
                m = len(importance)-1
            else:
                m -= 1