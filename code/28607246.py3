n = int(input())
for _ in range(n):
    N, M = input().split()
    data_list = list(map(int, input().split()))
    N = int(N)
    M = int(M)
    # 6 0
    # 1 1 9 1 1 9 8

    #출력 순서를 제작해보자
    #max인 값의 data_list내에서의 인덱스를 찾고 + 실제로 remove된 인덱스를 찾자
    final_max_dict = [{'index_data_list' : 'pop_index' }] # 여기다가 append 하는 방식
    item_own_dict = []
    count = 0

    #생성

    for item_index in range(len(data_list)):
        item_own_index = item_index
        item_own_hierarchy = data_list[item_index]
        item_own_dict_piece = [item_own_index,count]
        item_own_dict.append(item_own_dict_piece)
        
    item_new_dict = {}

    # print('data_list', data_list)
    # print('item_onw_dict', item_own_dict)
    while len(data_list) > 0:
        stand_data = max(data_list)
        stand_data_index = data_list.index(stand_data)
        left = data_list[:stand_data_index]
        right = data_list[stand_data_index+1:]
        left_own = item_own_dict[:stand_data_index]
        right_own = item_own_dict[stand_data_index+1:]
        data_list = right + left
        count += 1
        item_own_dict[stand_data_index][1] = count
        item_new_dict[item_own_dict[stand_data_index][0]] = item_own_dict[stand_data_index][1]
        # item_new_dict.append(item_own_dict[stand_data_index])
        item_own_dict = right_own + left_own
        
        # print('stand_data_index', stand_data_index)
        # print('data_list : ' , data_list)
        # print('item_new_dict : ', item_new_dict)
        
    print(item_new_dict[M])






