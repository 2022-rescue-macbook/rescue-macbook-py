def algorithm():
    nm_list = [int(x) for x in input().split()]
    num_list = [[int(x),0] for x in input().split()]
    temp_list = list()
    num_list[nm_list[1]][1] = 1
    temp = num_list[nm_list[1]][0]
    num_list = [x for x in num_list if x[0]>=temp]

    for x in range(nm_list[0]):
        check = num_list.index(max(num_list))
        if num_list[check][1]:
            result = len(num_list[:check]) + len(temp_list) + 1
            break
        front_list = num_list[:check]
        rear_list  = num_list[check:]
        num_list = rear_list + front_list
        temp_list.append(num_list[0])
        num_list.pop(0)

    return result


num = int(input())
result_list = list()
for x in range(num):
    result_list.append(algorithm())
for x in result_list:
    print(x)