test_case = int(input())
for i in range(test_case):
    num, m = map(int, input().split())
    print_list = list(map(int, input().split()))
    check_list = [0 for _ in range(num)] # [0, 0, 0, 0]
    check_list[m] = 1 # 궁금한 문서위치 저장

    count = 0
    while True:
        if print_list[0] == max(print_list): # 첫번째 값이 중요도가 가장 높다면
            count += 1

            if check_list[0] != 1:
                del print_list[0]
                del check_list[0]
            else:
                print(count)
                break
        else:
            print_list.append(print_list[0])
            check_list.append(check_list[0])
            del print_list[0]
            del check_list[0]