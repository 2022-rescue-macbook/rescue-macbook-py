import sys

def solution(priorities, location):
    answer = 0
    loc = [i for i in range(len(priorities))]
    while len(priorities) > 0:
        now = priorities[0]
        if max(priorities) > now:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
        else:
            priorities.pop(0)
            v = loc.pop(0)
            answer += 1
            if v == location:
                break
    return answer

test_case = int(input())
priority = []
for i in range(test_case):
    N_doc, location = map(int, sys.stdin.readline().rstrip().split())
    priority = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(priority, location))