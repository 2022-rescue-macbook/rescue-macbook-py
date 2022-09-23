test_case = int(input())
for i in range(test_case):
    n, m = list(map(int, input().split(' ')))
    lst = list(map(int, input().split(' ')))
    idx = list(range(len(lst)))
    order = 0

    while True:
        if lst[0] == max(lst):
            order += 1

            if idx[0] == m:
                print(order)
                break
            else:
                lst.pop(0)
                idx.pop(0)

        else:
            lst.append(lst.pop(0))
            idx.append(idx.pop(0))