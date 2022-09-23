def solution(priorities, location):
    answer = 0
    maximum = max(priorities)
    length = len(priorities)
    while 1 :
        if priorities[0] == maximum :
            answer += 1
            if location == 0 : return answer
            priorities.pop(0)
            maximum = max(priorities)
            location -= 1
            length -= 1
        else :
            if location : location -= 1
            else : location = length - 1
            priorities.append(priorities.pop(0))
            
    return answer

n = int(input())
for i in range(n) :
  a, b = map(int, input().split())
  priorities = list(map(int, input().split()))
  print(solution(priorities,b))