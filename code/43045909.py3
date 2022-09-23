n = int(input())

for i in range(n):
    d, q = map(int,input().split())
    inp = list(map(int, input().split()))
    queue = []
    for j in range(0,len(inp)):
        queue.append([j,inp[j]])

    result = 1

    while True:
        tmp = queue.pop(0)
        isNo = False

        for j in queue:
            if tmp[1] < j[1]:
                isNo= True
                break

        if not(isNo):
            if tmp[0] == q:
                print(result)
                break
            else:
                result += 1
        else:
            queue.append(tmp)







