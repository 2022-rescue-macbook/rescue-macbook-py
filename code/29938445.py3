def solution(cnt, target_idx, priority_arr):
    target_priority = priority_arr[target_idx]
    # 범위 줄이기
    indices = [idx for idx in range(cnt) if priority_arr[idx] >= target_priority]
    priorities = [p for p in priority_arr if p >= target_priority]
    printing_counter = 0
    while True:
        max_priority = max(priorities)
        check_idx = indices.pop(0)
        check_priority = priorities.pop(0)
        if check_priority == max_priority:
            printing_counter = printing_counter + 1
            if check_idx == target_idx:
                break
        else:
            indices.append(check_idx)
            priorities.append(check_priority)
    return printing_counter


if __name__ == '__main__':
    test_cnt = int(input())
    for i in range(test_cnt):
        paper_count, index_to_find = list(map(int, input().split()))
        priorities = list(map(int, input().split()))
        print_order = solution(paper_count, index_to_find, priorities)
        print(print_order)
