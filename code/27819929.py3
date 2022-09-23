def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split(" ")))

def get_order_of_document(priority_list, target):
    priority_list_with_origin_index = [[i, priority_list[i]] for i in range(len(priority_list))]
    sorted_priority_list_with_index = sorted(priority_list_with_origin_index, key= lambda x: (x[1], -x[0]), reverse=True)

    index = 0
    while True:
        elem = priority_list_with_origin_index.pop(0)
        if elem[1] == sorted_priority_list_with_index[0][1]:
            sorted_priority_list_with_index.pop(0)
            index += 1
            if target == elem[0]:
                break
        else:
            priority_list_with_origin_index.append(elem)
    return index



if __name__ == "__main__":
    test_case_num = read_int()
    results = []

    for i in range(test_case_num):
        [num_of_documents, target] = read_int_list()
        document_priority_list = read_int_list()
        order_of_document = get_order_of_document(document_priority_list, target)
        results.append(order_of_document)

    for result in results:
        print(result)
