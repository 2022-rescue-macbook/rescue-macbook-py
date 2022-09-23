for _ in range(int(input())):
    answer = 0
    n, m = map(int, input().split())
    arr = list(input().split())

    mv = max(arr)

    while True:
        v = arr.pop(0)
        if v == mv:
            answer += 1
            if m == 0:
                break
            else:
                m -= 1
            mv = max(arr)
        else:
            arr.append(v)
            if m == 0:
                m = len(arr)-1
            else:
                m -= 1
    print(answer)
