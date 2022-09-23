for _ in range(int(input())):
    a,index_Q = map(int,input().split())
    lst = list(map(int,input().split()))
    count = 0

    while 1:
        if max(lst) == lst[0]:
            if index_Q == 0:
                count += 1
                break
            del lst[0]
            count += 1
            index_Q -= 1
        
        else:
            if index_Q == 0:
                index_Q = len(lst)
            lst.append(lst[0])
            del lst[0]
            index_Q -= 1

    print(count)