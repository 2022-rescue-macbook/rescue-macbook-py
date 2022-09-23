def solution(n, m, printList):
  sortPriority = sorted(printList, reverse=True)
  answer = 0
  pointer = 0
  maxValue = sortPriority[answer]
  queue = []

  for idx, priority in enumerate(printList):
    queue.append((priority, idx))
  
  while len(queue) != 0:
    if maxValue <= queue[pointer][0]:
      answer += 1
      p = queue.pop(pointer)
      if p[1] == m:
        print(answer)
        break
      
      maxValue = sortPriority[answer]
    else:
      pointer += 1
    
    if pointer >= len(queue):
      pointer = 0
    
    
T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  printList = list(map(int, input().split()))
  solution(N, M, printList)
