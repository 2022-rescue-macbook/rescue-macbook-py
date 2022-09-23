case = int(input())


while (case):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    
    
    count = 0
    while True:
        count += 1
        printed = max(queue)
        printed_index = queue.index(printed)

        if printed_index == M:
            break
        
        M -= (1 + printed_index)
        if M < 0:
            M += N
        
        queue = queue[printed_index + 1:] + queue[:printed_index]
        N -= 1
            

    print(count)    
    
    case -= 1