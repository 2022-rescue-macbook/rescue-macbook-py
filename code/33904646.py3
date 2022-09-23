for _ in range(int(input())):
    n, m = map(int, input().split())
    _importance = list(map(int, input().split()))
    count = 0
    i = 0
    while True:
        if _importance[i] < max(_importance):
            i += 1
            if i == len(_importance):
                i = 0
        else:
            count += 1
            if i == m:
                print(count)
                break
            del _importance[i]
            if i < m:
                m -= 1
            if i == len(_importance):
                i = 0