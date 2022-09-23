t = int(input())
l = 0

while l<t :
    n,m = map(int,input().split())
    pri_list = list(map(int,input().split()))
    count = 1
    i = 0
    num_prt = m
    max_num_list = sorted(pri_list)

    max_num = max_num_list.pop()

    while True :
        if pri_list[i] != max_num :
            pri_list.append(pri_list[i])
            if num_prt == i :
                num_prt = len(pri_list)-1
            i+= 1

        else :
            if num_prt == i :
                print(count)
                break
            pri_list[i] = -1
            i+=1
            count += 1
            max_num = max_num_list.pop()

    l+=1