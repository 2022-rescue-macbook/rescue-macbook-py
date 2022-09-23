import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    lst = [0 for i in range(a)]
    lst[b] = 1
    count = 0
    while True:
        if nums[0] == max(nums):
            count += 1
            if lst[0] == 1:
                print(count)
                break
            else:
                del nums[0]
                del lst[0]
        else:
            nums.append(nums[0])
            del nums[0]
            lst.append(lst[0])
            del lst[0]