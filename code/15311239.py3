# coding=utf-8
N = int(input())
for i in range(N):
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    check = [1 for j in range(len(b))]
    start = 0
    end = a[0]-1
    count = 1
    while True:
        max = b[start]
        id_max = start
        if start < end:
            for j in range(start, end+1):
                if b[j] > max and check[j]:
                    max = b[j]
                    id_max = j
        else:  #start > end
            for j in range(start, a[0]):
                if b[j] > max and check[j]:
                    max = b[j]
                    id_max = j
            for j in range(0, end+1):
                if b[j] > max and check[j]:
                    max = b[j]
                    id_max = j
        for j in range(end, start):
            if b[j] > max and check[j]:
                max = b[j]
                id_max = j
        if id_max == a[1]:
            print(count)
            break
        check[id_max] = 0
        count += 1
        start = id_max
        end = id_max
        while check[start] == 0:
            if start == a[0] - 1:
                start = 0
            else:
                start += 1
        while check[end] == 0:
            if end == 0:
                end = a[0] - 1
            else:
                end -= 1

