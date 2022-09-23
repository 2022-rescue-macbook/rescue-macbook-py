import sys
testCase = int(input())

for _ in range(testCase):
    num, idx = tuple(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    max_arr = sorted(arr, reverse=True)
    j = 0
    k = 0
    while True:
        if arr[j] == max_arr[k]:
            cnt += 1
            if j == idx:
                print(cnt)
                break
            k += 1
        j = (j+1) % num