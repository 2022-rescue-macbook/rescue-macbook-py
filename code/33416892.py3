import sys

num = int(input())

for i in range(num):
    N, M = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))
    count = 1
    tmp = max(num_list)
    target = num_list[M]
    max_num_index = num_list.index(tmp)
    while num_list:
        if max_num_index == M:
            break
        else:
            count += 1
            num_list[max_num_index] = 0
            if max(num_list[max_num_index:]) >= max(num_list):
                tmp = max(num_list[max_num_index:])
                while tmp != num_list[max_num_index]:
                    max_num_index += 1
            else:
                tmp = max(num_list)
                max_num_index = num_list.index(tmp)
    print(count)