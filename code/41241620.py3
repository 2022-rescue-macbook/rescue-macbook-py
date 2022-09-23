result = []

for _ in range(int(input())):
  n, trace = map(int, input().split())
  li = list(map(int, input().split()))
  count = 1
  while True:
    if trace != 0:
      if li[0] != max(li):
        li.append(li.pop(0))
      else:
        del li[0]
        count += 1
      trace -= 1
    else:
      if li[0] == max(li):
        break
      else:
        li.append(li.pop(0))
        trace = len(li) - 1
  result.append(count)
  

for count in result:
  print(count)