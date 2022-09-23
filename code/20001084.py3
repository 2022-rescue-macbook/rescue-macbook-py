def set_pointer(N, pointer):
    if pointer >= N - 1:
        return 0
    else:
        return pointer + 1


for _ in range(int(input())):
    count = 0
    pointer = 0
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    while True:
        if queue[pointer] == max(queue):
            queue[pointer] = 0
            count += 1
            if pointer == M:
                break
            pointer = set_pointer(N, pointer)
        else:
            pointer = set_pointer(N, pointer)
    print(count)
