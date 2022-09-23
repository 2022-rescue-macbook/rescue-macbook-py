testcase = int(input())

for _ in range(testcase):
    n, point = map(int, input().split())
    que = list(map(int, input().split()))
    chk = [0 for _ in range(n)]
    chk[point] = 1

    count = 0
    while True:
        if que[0] == max(que):
            count += 1
            if chk[0] == 1:
                print(count)
                break
            else:
                que.pop(0)
                chk.pop(0)
        else:
            que.append(que.pop(0))
            chk.append(chk.pop(0))

