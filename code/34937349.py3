from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    m,n = map(int, stdin.readline().split(" "))
    arr = list(map(int, stdin.readline().split(" ")))
    max_priority_arr = arr.copy()
    max_priority_arr.sort()
    result_check = 0
    index = 0
    while True:
        if arr[index] < max_priority_arr[-1]:
            arr.append(arr[index])
            if index == n:
                n = len(arr)-1
        else:
            max_priority_arr.pop()
            result_check += 1
            if index == n:
                break
        index += 1
    print(result_check)