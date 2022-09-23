import sys
T = int(input())
answer = []
for _ in range(T):
    count = [0 for i in range(10)]
    num = 0
    cur = -1
    N, M = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        count[array[i] - 1] += 1
        array[i] = [i, array[i]]
    while cur != M:
        prt = True
        for i in range(array[0][1], 10, 1):
            if count[i] > 0:
                array.append(array.pop(0))
                prt = False
                break
        if prt is True:
            count[array[0][1] - 1] -= 1
            cur = array.pop(0)[0]
            num += 1
    answer.append(num)
    
for i in answer:
    print(i)