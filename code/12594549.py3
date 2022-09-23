T = int(input())

for _ in range(T):
    N, num = map(int, input().split())
    queuelist = list(map(int, input().split()))
    count = 0
    while True:
        idx = queuelist.index(max(queuelist))
        if idx != 0:
            for i in range(idx):
                temp = queuelist.pop(0)
                queuelist.append(temp)
                if num == 0:
                    num = len(queuelist)-1
                else:
                    num -= 1
        queuelist.pop(0)
        count += 1
        if num == 0:
            break
        num -= 1
    print(count)

