def func(n, idx, lst):
    if n == 1: return 1
    
    queue = []
    for i, v in enumerate(lst):
        queue.append([i,v])
    cnt = 0
    while lst:
        _max = max(lst)
        while True:
#             print(queue, lst)
            if queue[0][1] != _max:
                a,b = queue.pop(0)
                queue.append([a,b])
            else:
                cnt += 1
                a,b = queue.pop(0)
                if a == idx:
                    return cnt
                lst.remove(_max)
                break

N = int(input())
for _ in range(N):
    n, idx = map(int, input().split())
    lst = list(map(int, input().split()))
    print(func(n, idx, lst))