import sys 
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    tmp = [0]*n
    tmp[m] = 1
    cnt = 0
    
    while True:
        if q[0] == max(q):
            cnt += 1
            if tmp[0] == 1:
                print(cnt)
                break
            else:
                del q[0]
                del tmp[0]
        else:
            q.append(q[0])
            del q[0]
            tmp.append(tmp[0])
            del tmp[0]