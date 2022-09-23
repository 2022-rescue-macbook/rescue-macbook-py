import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, target = map(int, input().split())
    numbers = list(map(int, input().split()))
    std = sorted(numbers)

    i = 0
    cnt = 0
    while True:
        i %= N
        if numbers[i] == std[-1]:
            std.pop()
            cnt += 1
            if i == target:
                print(cnt)
                break
        i += 1
