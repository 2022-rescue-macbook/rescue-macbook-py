for _ in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    idx = list( False for _ in range(len(priority)))
    idx[M] = True
    cnt = 0
    while priority:
        if priority[0] != max(priority):
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))
        else:
            cnt += 1
            if idx[0]:
                print(cnt)
                break
            else:
                priority.pop(0)
                idx.pop(0)
