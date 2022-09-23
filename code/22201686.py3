t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    d = list(map(int, input().split(' ')))
    order = sorted(d, reverse=True)
    max_index = 0
    q = [(i, idx) for idx, i in enumerate(d)]
    count = 0

    while True:
        if q[0][0] == order[max_index]:
            count += 1
            max_index += 1
            if q[0][1] == m:
                print(count)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))