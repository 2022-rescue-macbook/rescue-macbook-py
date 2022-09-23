T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    for idx in range(len(li)):
        li[idx] = [li[idx], idx]
    cnt = 0
    f = 0
    while True:
        max_v = 0
        for i in range(len(li)):
            if max_v < li[i][0]:
                max_v = li[i][0]
        value = [0, 0]
        while value[0] != max_v:
            value = li.pop(0)

            if value[0] == max_v:
                if value[1] == M:
                    print(cnt+1)
                    f = 1
                    break
                else:
                    cnt += 1
                    break
            else:
                li.append(value)
        if f:
            break
