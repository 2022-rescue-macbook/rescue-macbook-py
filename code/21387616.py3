TEST_CASE = int(input())

for _ in range(TEST_CASE):
    N, M = map(int, input().split())
    weight_list = str.strip(input())

    if len(weight_list) == 1:
        print(1)
        continue
    weight_list = list(map(int, weight_list.split()))

    for i in range(len(weight_list)):
        weight_list[i] = (i, weight_list[i])

    max_value = max(weight_list, key=lambda weight: weight[1])
    print_count = 1
    while True:
        if weight_list[0] != max_value:
            weight_list.append(weight_list.pop(0))
        else :
            data = weight_list.pop(0)
            if data[0] != M:
                print_count += 1
            else :
                print(print_count)
                break
            max_value = max(weight_list, key=lambda weight: weight[1])
