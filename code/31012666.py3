case = int(input())

result = []

for i in range(case):

    n, m = list(map(int, input().split(" ")))
    queue = list(map(int, input().split(" ")))
    
    k = queue[m]
    max_value = max(queue)
    count = 1

    while True:
        
        if max_value == k and m == 0:
            break
        else:
            data = queue[0]
            queue.pop(0)
            if max_value == data:
                max_value = max(queue)
                count += 1
            else:
                queue.append(data)
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1

    result.append(str(count))

print("\n".join(result))
