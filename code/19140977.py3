from sys import stdin

case = int(stdin.readline())

for _ in range(case) :
    N,M = map(int, stdin.readline().split())
    que = list(map(int, stdin.readline().split()))
    check = [0 for _ in range(N)]
    check[M] = 1
    count = 0
    while True :
        if que[0] == max(que) :
            count += 1
            if check[0] == 1 :
                print(count)
                break
            else :
                que.pop(0)
                check.pop(0)
        else :
            que.append(que.pop(0))
            check.append(check.pop(0))
