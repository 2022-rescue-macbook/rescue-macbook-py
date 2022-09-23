import sys
case = int(input())

for _ in range(case):
    result = 0
    N, C = map(int, input().split())
    importance = list(map(int, sys.stdin.readline().rstrip().split()))
    while 1:
        if importance[0] == max(importance):
            if C:
                importance.pop(0)
                C -= 1
                result += 1
            else:
                print(result + 1)
                break
        else:
            if C:
                importance.append(importance.pop(0))
                C -= 1
            else:
                importance.append(importance.pop(0))
                C = len(importance) - 1