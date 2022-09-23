from sys import stdin


test_cases = int(stdin.readline())

for _ in range(test_cases):
    n, m = list(map(int, stdin.readline().split()))
    important = list(map(int, stdin.readline().split()))
    idx = list(range(len(important)))
    idx[m] = "target"

    order = 0

    while True:
        if important[0] == max(important):
            order += 1

            if idx[0] == "target":
                print(order)
                break
            else:
                important.pop(0)
                idx.pop(0)
        else:
            important.append(important.pop(0))
            idx.append(idx.pop(0))
