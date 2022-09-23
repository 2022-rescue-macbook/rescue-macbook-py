case = int(input())
for i in range(case):
    n, a = map(int, input().split())
    ind = [x for x in range(n)]
    check = ind[a]
    lst = [int(x) for x in input().split()]
    count = 0
    while(True):
        flag = True
        now1 = lst[0]
        now2 = ind[0]
        lst.remove(now1)
        ind.remove(now2)
        if len(lst) != 0:
            for j in lst:
                if (now1 < j):
                    lst.append(now1)
                    ind.append(now2)
                    flag = False
                    break
        if (flag):
            count += 1
            if check == now2:
                print(count)
                break
