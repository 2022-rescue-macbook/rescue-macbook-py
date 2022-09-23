for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [(i, int(x)) for i, x in enumerate(input().split())]
    brr = sorted(arr, key=lambda x: -x[1])
    index, value = arr[M]
    answer = 1
    state = False
    while True:
        b_index, b_value = brr.pop(0)
        while True:
            a_index, a_value = arr.pop(0)
            if b_value == value and a_index == index:
                print(answer)
                state = True
                break
            if a_value < b_value:
                arr.append((a_index, a_value))
            else:
                answer += 1
                break
        if state:
            break
