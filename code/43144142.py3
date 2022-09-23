import sys

test_cases = int(sys.stdin.readline())

for i in range(test_cases) :
  n, m = map(int, sys.stdin.readline().split())
  important = list(map(int, sys.stdin.readline().split()))

  array = [0]*n
  array[m] = 'target'
  order = 0
  
  while True : 
    if important[0] == max(important) :
      order += 1
      if array[0] == 'target' :
        print(order)
        break;
      else :
        array.pop(0)
        important.pop(0)
    else :
      important.append(important.pop(0))
      array.append(array.pop(0))