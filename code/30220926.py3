test_num = int(input())
flag = True

for i in range(test_num):
    flag=True
    num, idx = list(map(int, input().split()))
    value = list(map(int, input().split()))

    idx_list = [i for i in range(num)]
    cnt = 0

    while(flag==True):
        max_idx = value.index(max(value))

        while(max_idx!=0):
            value.append(value.pop(0))
            idx_list.append(idx_list.pop(0))
            max_idx = value.index(max(value))
        del value[0]
        cnt+=1
        if(idx == idx_list[0]):
            print(cnt)
            flag=False
        del idx_list[0]

