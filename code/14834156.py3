num = int(input())

for i in range(0, num):
    n, m = input().split()
    n = int(n)
    m = int(m)

    q_list = input().split()
    chk_list = []

    for x in range(0, n):
        chk_list.append(x)

    count = 0
    while True:
        if q_list[0] == max(q_list):
            count += 1
            if chk_list[0] == m:
                print(count)
                break
            else:
                q_list.pop(0)
                chk_list.pop(0)
        else:
            q_list.append(q_list.pop(0))
            chk_list.append(chk_list.pop(0))