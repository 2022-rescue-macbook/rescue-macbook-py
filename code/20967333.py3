k = int(input())
n = []
arr = []
for _ in range(k):
    n.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
for i in range(k):
    q = arr[i]
    index = list(range(len(q)))
    count = 0
    while q:
        if q[0] != max(q):
            q.append(q.pop(0))
            index.append(index.pop(0))
        else:
            b = q.pop(0)
            count += 1
            if index[0] == n[i][1]:
                break
            else:
                index.pop(0)
    print(count)
