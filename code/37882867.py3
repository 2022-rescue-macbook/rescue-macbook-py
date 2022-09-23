import sys

input = sys.stdin.readline


def solution(priorities, location):
    idx_list = list(range(len(priorities)))
    result = []
    
    while True:
        i = priorities.index(max(priorities))
        result.append(priorities[i])
        if idx_list[i] == location:
            return len(result)
        else:
            priorities = priorities[i+1:] + priorities[:i]
            idx_list = idx_list[i+1:] + idx_list[:i]


case = int(input())

for _ in range(case):
    n, target_idx = map(int, input().split())
    queue = list(map(int, input().split()))
    
    print( solution(queue, target_idx) )