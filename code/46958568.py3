number = int(input());

for _ in range(number):
  a,b = map(int, input().split())
  arr = list(map(int, input().split()))
  r = 1
  while arr:
    if arr[0] >= max(arr):
      arr.pop(0)
      if b == 0:
        print(r)
        break
      else:
        b -= 1
        r += 1

    else:
      arr.append(arr.pop(0))
      if b == 0: 
        b = len(arr) - 1
      else:
        b -= 1