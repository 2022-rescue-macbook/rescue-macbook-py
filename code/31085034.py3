T = int(input())
left=0
for _ in range(T):
  N,M = map(int, input().split())
  important = list(map(int,(input().split())))
  seat = M
  count = 0
  while (1):
    maxNum = max(important)
    for _ in range(len(important)):
      if important[0] == maxNum:
        break
      else:
        if seat != 0:
          seat -= 1
          important.append(important.pop(0))
        else:
          seat = len(important)-1
          important.append(important.pop(0))
    if seat==0:
      count+=1
      break
    if important[0] == maxNum:
      important.pop(0)
      count +=1
      seat -= 1
  print(count)
