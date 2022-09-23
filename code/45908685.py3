import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num, position = map(int, input().split())
    nums = list(map(int, input().split()))
    ord = list(range(len(nums)))
    ord[position] = 'target'

    order = 0

    while True:
        if nums[0] == max(nums):
            order += 1

            if ord[0] == 'target':
                print(order)
                break
            else:
                nums.pop(0)
                ord.pop(0)
        else:
            nums.append(nums.pop(0))
            ord.append(ord.pop(0))