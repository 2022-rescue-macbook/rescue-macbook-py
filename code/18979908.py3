t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    importance = list(map(int, input().split()))

    dict = {}
    for i in range(0, len(importance)):
        dict[i] = importance[i]
    
    queue = [i for i in range(n)]


    cnt = 1
    result = [0] * n

    while queue:
        first = queue.pop(0)
        if dict[first] == max(importance):
            importance.remove(max(importance))
            result[first] = cnt
            cnt += 1
        else:
            queue.append(first)
    
    print(result[m])
