for i in range(int(input())):
    x, y = input().split()
    x = int(x)
    y = int(y)

    qu = list(map(int, input().split()))
    qu = [[qu[i], i] for i in range(x)]
    m = max(qu[i][0] for i in range(len(qu)))

    order = 0
    c = 1

    while c:
        for i in range(len(qu)):
            t = qu.pop(0)
            if(t[0] == m):
                order += 1
                if(t[1] == y):
                    c = 0
                    break
                m = max(qu[i][0] for i in range(len(qu)))
            else:
                qu.append(t)

    print(order)
