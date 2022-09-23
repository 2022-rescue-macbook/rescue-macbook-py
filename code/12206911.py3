T = int(input())

for _ in range(T):
    N, M = map(int, input().split())  # num of doc, index

    values = list(map(int, input().split(" ")))
    checker = [False] * N
    checker[M] = True

    # print(checker)

    count = 0
    while values:
        if values[0] == max(values):
            count += 1
            if checker[0]:
                break
            values.pop(0)
            checker.pop(0)
        else:
            values.append(values.pop(0))  # move lower priority doc
            checker.append(checker.pop(0))

    print(count)