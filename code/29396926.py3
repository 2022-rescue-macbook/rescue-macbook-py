import sys

testcase_num = int(sys.stdin.readline())
result = []

for _ in range(testcase_num):
    _, target = map(int, sys.stdin.readline().split(' '))
    priority = list(map(int, sys.stdin.readline().split(' ')))
    tmp = 0

    while priority:
        if len(priority) == 1 or priority[0] >= max(priority[1:]):
            priority.pop(0)
            
            tmp += 1
            if target == 0:
                result.append(tmp)
                break
        else:
            priority = priority[1:]+[priority[0]]
        target = target - 1 if target else len(priority)-1

sys.stdout.write('\n'.join(map(str, result)))