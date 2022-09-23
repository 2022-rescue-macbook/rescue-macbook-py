for _ in range(int(input())):
    n, m = map(int, input().split(' '))
    que = list(map(int, input().split(' ')))
    chk = ['T' if i == m else 0 for i in range(n)]

    count = 0
    while True:
        if que[0] == max(que):
            count += 1
            if chk[0] == 'T':
                print(count)
                break
            else:
                que.pop(0)
                chk.pop(0)
        else:
            que.append(que.pop(0))
            chk.append(chk.pop(0))