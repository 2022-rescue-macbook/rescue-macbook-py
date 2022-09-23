import sys
sinput = sys.stdin.readline

TN = int(sinput())

for _ in range(TN):
    N, M = map(int, sinput().split())
    test_list = list(map(int, sinput().split()))
    num = test_list[M]
    test_list[M] = 0
    max_num = max(test_list)
    itr, count, last_itr, len_list = 0, 0, 0, len(test_list)
    while max_num > num:
        for _ in range(len_list):
            if itr == len_list: itr = 0

            if test_list[itr] == max_num:
                test_list.pop(itr)
                count += 1
                len_list -= 1
                last_itr = itr
            else: itr += 1
        max_num -= 1
        itr = last_itr

    else:
        for _ in range(len_list):
            if itr == len_list: itr = 0

            if test_list[itr] == max_num:
                test_list.pop(itr)
                count += 1
                len_list -= 1
            elif test_list[itr] == 0:
                count += 1
                break
            else: itr += 1
    print(count)