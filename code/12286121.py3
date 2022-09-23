for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = input().split()
    queue = [int(i) for i in queue]
    count = 1
    while queue:
        if queue[0] == max(queue):
            if m == 0:
                print(count)
                break
            else:
                queue = queue[1:]
                m -= 1
                count += 1
        else:
            queue = queue[1:] + [queue[0]]
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1