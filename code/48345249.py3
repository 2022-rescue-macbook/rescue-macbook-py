import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, M = map(int, input().rstrip().split())
    priority = list(map(int, input().rstrip().split()))
    idx = list(range(N))
    idx[M] = 'target'
    
    count = 0
    
    while True:
        if len(priority) >= 1:
            if priority[0] < max(priority):
                priority.append(priority.pop(0))
                idx.append(idx.pop(0))
    
            else:
                count += 1
                if idx[0] == 'target':
                    break
                priority.pop(0)
                idx.pop(0)
            
        else:
            break
            
    print(count)