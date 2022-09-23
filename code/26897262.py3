from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    N,M = map(int, stdin.readline().split())
    importance = list(map(int,stdin.readline().split()))
    queue = []
    i = 1

    for _ in range(N):
        queue.append(False)
    
    queue[M] = True
    choice = importance[M]
    
    while choice:
        if importance[0] == max(importance):

            if queue[0] == True:
                print(i)
                break

            else:
                importance.pop(0)
                queue.pop(0)
                i = i + 1
            
        else:
            importance.append(importance.pop(0))
            queue.append(queue.pop(0))
            
