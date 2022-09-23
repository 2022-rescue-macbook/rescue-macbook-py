from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    ans = 0
    N, M = map(int, stdin.readline().rstrip().split())
    pr = list(map(int, stdin.readline().rstrip().split()))
    left_nums = [0] * 10
    l = 9
    for n in pr:
        left_nums[n] += 1

    e = [[p, i] for i, p in enumerate(pr)]

    while left_nums[-1] == 0:
        left_nums.pop()
        l -= 1

    while e[0][0] != l:
        e.append(e[0])
        del e[0]

    pop_num = e[0][1]
    left_nums[e[0][0]] -= 1
    ans += 1
    del e[0]

    while pop_num != M:
        while left_nums[-1] == 0:
            left_nums.pop()
            l -= 1

        while e[0][0] != l:
            e.append(e[0])
            del e[0]
        pop_num = e[0][1]

        left_nums[e[0][0]] -= 1
        del e[0]
        ans += 1
    print(ans)
