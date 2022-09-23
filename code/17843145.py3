import sys

# T = int(input())
T = int(sys.stdin.readline())

for i in range(T):
#     N, M = list(map(int, input().split()))
    N, M = list(map(int, sys.stdin.readline().split()))
#     imp_arr = list(map(int, input().split()))
    imp_arr = list(map(int, sys.stdin.readline().split()))
    flag_arr = [0 for _ in range(N)]
    flag_arr[M] = 1
    count = 0
    if len(imp_arr) == N:
        while True:
            if imp_arr[0] == max(imp_arr):
                count += 1
                if flag_arr[0] == 1:
                    print(count)
                    break
                else:
                    del imp_arr[0]
                    del flag_arr[0]
            else:
                imp_arr.append(imp_arr.pop(0))
                flag_arr.append(flag_arr.pop(0))