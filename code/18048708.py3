TESTCASE = int(input())

for i in range(TESTCASE):
    M, N = list(map(int, input().split()))
    array = [c for c in range(M)]
    dictionary = {}
    cnt = 1

    if M == 1:
        K = [int(input())]
    else:
        K = list(map(int, input().split()))

    while True:
        if len(K) == 1:
            dictionary[array.pop(0)] = cnt
            break

        if max(K) != K[0]:
            K.append(K.pop(0))
            array.append(array.pop(0))
        else:
            K.pop(0)
            dictionary[array.pop(0)] = cnt
            cnt += 1

    print(dictionary[N])

