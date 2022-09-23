n = int(input())
for i in range(n):
    k, num = map(int, input().split())
    L = list(map(int, input().split()))
    loop = 0
    flag = 0
    count = 0
    while L:
        if loop == num:
            flag = 1
        if L[0] != max(L):
            L.append(L.pop(0))
            if flag:
                num = len(L)
                loop = 0
            flag = 0
        else:
            L.pop(0)
            count += 1
            if flag:
                print(count)
                break
        loop += 1
