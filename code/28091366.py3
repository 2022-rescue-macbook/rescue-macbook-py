tn = int(input())
result = []

for _ in range(tn):
    n, idx = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0
    
    while queue:
        if queue[0] == max(queue):
            queue.pop(0)
            cnt += 1
            if idx == 0:
                break
            else:
                idx -= 1
        else:
            queue.append(queue.pop(0))
            if idx == 0:
                idx = len(queue)-1
            else:
                idx -= 1
    result.append(cnt)

print("\n".join(map(str, result)))