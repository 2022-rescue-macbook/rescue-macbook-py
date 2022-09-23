import sys

K = int(sys.stdin.readline())

for i in range(K) :
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    idx = list(range(N))
    idx[M] = 'tg'

    result = 0

    while True :
        if nums[0] == max(nums) :
            result += 1

            if idx[0] == 'tg' :
                print(result)
                break
            else :
                nums.pop(0)
                idx.pop(0)
        else :
            nums.append(nums.pop(0))
            idx.append(idx.pop(0))