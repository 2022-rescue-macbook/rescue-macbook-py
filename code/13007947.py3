tc = int(input())
for i in range(tc):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    count=0
    d = b
    while 1:
        while c[0] != max(c):
            c.append(c[0])
            del c[0]
            d = d-1

        count = count+1
        if d == 0:
            print(count)
            break
        else:
            d = d%len(c)
            del c[0]
            d = d-1