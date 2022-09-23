import sys



n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    pr = list(map(int, sys.stdin.readline().split()))
    idx = [0 for i in range(a)]
    idx[b] = 1
    cnt = 0
    
    while True:
        
        if pr[0] == max(pr):
            cnt+=1
            if idx[0] == 1:
                print(cnt)
                break
            else:
                del pr[0]
                del idx[0]

        else:
            pr.append(pr[0])
            del pr[0]
            idx.append(idx[0])
            del idx[0]