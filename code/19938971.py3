test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    priority = [int(x) for x in input().split()]
    queue = [(i, p) for i, p in enumerate(priority)]
    
    count = 0
    
    while True:
        max_value = max(queue, key=lambda x:x[1])[1]
        
        while queue[0][1] != max_value:
            queue.append(queue.pop(0))
        
        doc = queue.pop(0)
        
        if doc[0] == M:
            count += 1
            print(count)
            break
            
        else:
            count += 1