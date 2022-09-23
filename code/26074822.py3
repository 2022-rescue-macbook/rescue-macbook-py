n = int(input())

order = []
for i in range(n):
    m, p = list(map(int, input().split(' ')))
    queue = list(map(int,input().split(' ')))
    index = p
    count = 0
    while len(queue) > 0:
        if queue[0] == max(queue):
            if index == 0:
                count += 1
                order.append(count)
                break
            else:
                index -= 1
                count += 1
                del queue[0]
        else:
            temp = queue[0]
            del queue[0]
            queue.append(temp)
            if index == 0:
                index = len(queue) - 1
            else:
                index -= 1

for s in order:
    print(s)