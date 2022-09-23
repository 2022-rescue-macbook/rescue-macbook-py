def printQueue(find, queue): # find = 2, queue = [1 2 3 4]
    rank = queue[:]
    rank.sort(reverse=True)
    findIndex = find
    count = 0
    while rank:
        if rank[0] == queue[0]:
            rank.pop(0)
            queue.pop(0)
            count += 1
            if findIndex == 0:
                break
            findIndex -= 1
        else:
            queue.append(queue.pop(0))
            if findIndex == 0:
                findIndex = len(queue) - 1
            else:
                findIndex -= 1
    return count

result = list()
n = int(input())
for i in range(n):
    find = int(input().split()[1])
    queue = list(map(int, input().split()))
    result.append(printQueue(find, queue))

for i in range(n):
    print(result[i])