import sys
a = int(sys.stdin.readline())
for l in range(a):
    NM = list(map(int,sys.stdin.readline().split()))
    m = NM[0]
    n = NM[1]
    order = list(map(int, sys.stdin.readline().split()))

    result = 0
    while len(order) > 0:
        i = 0
        temp = order[0]
        for k in range(1,len(order)):
            if temp < order[k]:
                order.pop(0)
                order.append(temp)
                i += 1
                if n == 0:
                    n = len(order)-1
                else:
                    n -= 1
                break
    
        if i == 0 and n == 0:
            order.pop(0)
            result += 1
            print(result)
            break
        elif i == 0 and n != 0:
            order.pop(0)
            result += 1
            n -= 1
    