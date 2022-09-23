# https://www.acmicpc.net/problem/1966

# 4, 2 / 1, 2, 3, 4 / [2] = 3
# 4,3,2,1 /  

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
  n, m = map(int, stdin.readline().split(' '))
  priorityArray = list(map(int, (stdin.readline().split(' '))))

  x = priorityArray[m] # save priority of m to x

  count = 1

  while True:   
    if m == 0 and max(priorityArray) == priorityArray[0]:
      print(count)
      break

    if max(priorityArray) == priorityArray[0]:
      del priorityArray[0]
      count += 1
      m -= 1
    
    else:
      priorityItem = priorityArray[0]
      priorityArray = priorityArray[1:]
      priorityArray.append(priorityItem)
      
      if m == 0:
        m = len(priorityArray) - 1
      else: 
        m -= 1
      
    
