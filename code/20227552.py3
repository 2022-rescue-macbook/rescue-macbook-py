case = int(input())
for i in range(case): 
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))       
    priority_finder = [0 for i in range(n)]   
    priority_finder[m] = "True"                  
    count = 0
    while True:
        if queue[0] == max(queue):    
            count += 1                
            if priority_finder[0] == "True": 
                print(count)
                break
            else:
                del queue[0]
                del priority_finder[0]
        else:
            queue.append(queue[0])
            del queue[0]
            priority_finder.append(priority_finder[0])
            del priority_finder[0]
