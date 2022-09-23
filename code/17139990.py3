def pro(lst):
    global tar
    cnt = 0
    while 1:
        # print(lst)
        maxi = max(lst)
        # print(tar)
        if lst[0] == maxi:
            cnt += 1
            if tar == 0:
                return cnt
            lst.pop(0)
            tar -= 1
        else:
            tmp = lst.pop(0)
            if tar == 0:
                tar = len(lst)
            else:
                tar -= 1
            lst.append(tmp)


test = int(input())
for testCase in range(1, 1 + test):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    tar = m
    ret = pro(lst)

    print(ret)
