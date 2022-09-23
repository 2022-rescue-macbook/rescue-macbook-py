case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    const = list(zip([k for k in range(N)], num_list))
    cnt = 0

    for i in range(10000):
        if const[0][1] == max(num_list):
            a, b = const.pop(0)
            num_list.remove(max(num_list))
            cnt += 1
            if a == M:
                break
        else:
            c = const.pop(0)
            const.append(c)

    print(cnt)