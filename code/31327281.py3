n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    z = list(map(int, input().split()))
    list1 = [0 for j in range(x)]
    list1[y] = 1
    flag = 0

    while True:
        if z[0] == max(z):
            flag += 1
            if list1[0] == 1:
                print(flag)
                break
            else:
                del list1[0]
                del z[0]
        else:
            z.append(z[0])
            del z[0]
            list1.append(list1[0])
            del list1[0]
