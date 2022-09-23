for i in range(int(input())):
    size, target = map(int, input().split())
    que = list(map(int, input().split()))
    check = [0 for i in range(len(que))]
    check[target] = 1

    count = 0
    while True:
        if que[0] == max(que):
            count += 1
            if check[0] == 1:
                print(count)
                break
            else:
                que.pop(0)
                check.pop(0)
        else:
            que.append(que.pop(0))
            check.append(check.pop(0))