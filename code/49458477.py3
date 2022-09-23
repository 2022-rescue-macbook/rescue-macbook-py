import sys
case = int(sys.stdin.readline())
for i in range(case):
    queue = []
    N,M = map(int,sys.stdin.readline().split())
    count =0
    queue = list(map(int,sys.stdin.readline().split()))
    pointer = M
    sorted_queue = sorted(queue,reverse=True)
    while True:
        if queue[0] == sorted_queue[0] and pointer == 0:
            count +=1
            print(count)
            break
            
        elif queue[0] == sorted_queue[0]:
            count +=1
            sorted_queue.pop(0)
            queue.pop(0)
            pointer = (pointer-1)% len(queue)
        else:
            queue.append(queue.pop(0))
            pointer = (pointer-1)% len(queue)