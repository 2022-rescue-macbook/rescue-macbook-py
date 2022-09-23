t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    target = [data[m], m]
    temp = []
    for i in range(n):
        temp.append([data[i], i])
    q = []
    if len(data) == 1:
        print(1)
    else:
        while True:
            if len(data) == 0:
                break
            if data[0] < max(data):
                data.append(data.pop(0))
                temp.append(temp.pop(0))
            else:
                data.pop(0)
                q.append(temp.pop(0))
        print(q.index(target)+1)