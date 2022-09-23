test_num = int(input())

for test_times in range(test_num):
    doc_num, target_doc = list(map(int, input().split(' ')))
    important = list(map(int, input().split(' ')))
    index_list = list(map(int, range(len(important))))
    target_check = -1
    count = 0
    while target_check != target_doc:
        
        if max(important) == important[0]:
            important.pop(0)
            target_check = index_list.pop(0)
            count += 1
        else:
            temp = important.pop(0)
            important.append(temp)
            temp_index = index_list.pop(0)
            index_list.append(temp_index)

    print(count)
    