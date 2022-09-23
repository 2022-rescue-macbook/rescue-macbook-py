case = int(input())
for i in range(case):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    index = 0
    num = 1
    rep = True
    for k in range(9, 0, -1):
        if not rep:
            break
        while k in lst:
            # print("k", k)
            if lst[index] == k:
                if index == M:
                    print(num)
                    rep = False
                lst[index] = 0
                num += 1
            index += 1
            index %= N