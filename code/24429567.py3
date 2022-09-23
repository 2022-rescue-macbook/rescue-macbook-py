import sys

input = sys.stdin.readline

T = int(input())

for x in range(T):
    answer = 0
    count = 0
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    num = [x for x in range(n)]

    while arr:
        if arr[0] == max(arr):
            count += 1

            if num[0] == m:
                answer = count

            del num[0]
            del arr[0]
        else:
            arr.append(arr[0])
            num.append(num[0])
            del num[0]
            del arr[0]

    print(answer)