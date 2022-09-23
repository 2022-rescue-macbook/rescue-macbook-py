import sys
input = sys.stdin.readline
case = int(input())
for _ in range(case):
    n,m = map(int,input().split())
    important = list(map(int,input().split()))
    check = [0 for _ in range(n)]
    check[m] = 1
    cnt = 0 
    while True:
        if important[0] == max(important):
            cnt+=1
            if check[0]==1:
                print(cnt)
                break
            else:
                important.pop(0)
                check.pop(0)
        else:
            important.append(important.pop(0))
            check.append(check.pop(0))


