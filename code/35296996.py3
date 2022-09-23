n = int(input())

result = []

for i in range(n):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))

    queue = [(C[i], i) for i in range(len(C))]

    count = 0
    while True:
        tmp = queue.pop(0)
        if tmp[0] == max(C):
            count += 1
            if tmp[1] == M:
                break
            C.remove(tmp[0])
        else:
            queue.append(tmp)

    result.append(count)

for r in result:
    print(r)