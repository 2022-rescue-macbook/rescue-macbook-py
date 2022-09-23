n = int(input())

for _ in range(n):
    target = list(map(int, input().split()))[1]
    queue = list(map(int, input().split()))
    order = list(range(len(queue)))
    out_count = 0
    while queue:
        max_val = max(queue)
        if queue[0] < max_val:
            max_index = queue.index(max_val)
            for _ in range(max_index):
                queue.append(queue.pop(0))
                order.append(order.pop(0))
            value, idx = queue.pop(0), order.pop(0)
            out_count += 1
            if idx == target:
                print(out_count)
        else:
            value, idx = queue.pop(0), order.pop(0)
            out_count += 1
            if idx == target:
                print(out_count)