import sys

test_cases = int(input())

for a in range(test_cases):
  # input
  n,target = list(map(int,sys.stdin.readline().split( )))
  important = list(map(int,sys.stdin.readline().split( )))
  
  count = 0
  
  while True:
    if important[0] == max(important):
      # 출력
      important.pop(0)
      count+=1
      if target == 0:
        break
      else:
        target -= 1
    else:
      # 맨 뒤로 넘김
      important.append(important.pop(0))
      if target == 0:
        target = len(important)
      target -= 1

  print(count)