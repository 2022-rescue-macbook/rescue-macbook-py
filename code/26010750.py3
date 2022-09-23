from sys import stdin
#Test case
test_case = int(stdin.readline())
#result
result = []
#printer
for i in range(test_case):
    counter = 0
    #N,M
    N, M = list(map(int,stdin.readline().split(' ')))
    #queue
    queue = list(map(int,stdin.readline().split(' ')))
    index = list(range(N))
    #Max distinguish
    while True:
        if queue[0] == max(queue):
            counter += 1
            if index[0] == M:
                result.append(counter)
                break
            else:
                queue.pop(0)
                index.pop(0)
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))
#submit
print('\n'.join(map(str,result)))
