import sys
T = int(input())
for _ in range(T):
    count = 0
    length,location = map(int,input().split())
    queue = list(map(int,sys.stdin.readline().rstrip().split()))
    Max = max(queue)
    index = 0
    while 1:
        if Max == queue[index]:
            count += 1
            queue[index] = -1
            Max = max(queue)
        if queue[location] == -1:
            break
        if index != length -1:
            index += 1
        else:
            index = 0
    print(count)
