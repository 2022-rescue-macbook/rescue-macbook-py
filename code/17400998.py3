for _ in range(int(input())):
    n, m = map(int, input().split())
    rank_list = [int(i) for i in input().split()]
    mutable_list = rank_list.copy()
    index_list = [i for i in range(n)]
    
    cnt = 1
    while index_list:
        if rank_list[index_list[0]] == max(mutable_list):
            current_index = index_list.pop(0)
            if current_index == m:
                break

            mutable_list.remove(max(mutable_list))
            cnt += 1
        else:
            index_list.append(index_list.pop(0))
    print(cnt)