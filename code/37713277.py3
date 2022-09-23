import sys


def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1


n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    print(solution(data, y))
