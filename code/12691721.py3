import sys
test_num = int(sys.stdin.readline().rstrip())
for i in range(test_num):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    queue = list(sys.stdin.readline().rstrip().split())
    queue = [int(i) for i in queue]
    interest = queue[M]
    order = 0
    
    while queue:
    
        important = max(queue)
        
        if (M == 0 and queue[0] == important):
            order += 1
            break
        else:
            pass
        
        if queue[0] != important:
            queue.append(queue.pop(0))
    
        else:
            queue.pop(0)
            order += 1
            if queue == []:
                break
            else:
                pass
    
        M -= 1
    
        if M == -1:
            M = len(queue) - 1
        else:
            pass
    print(order)