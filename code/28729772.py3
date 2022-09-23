import sys
r = sys.stdin.readline

case = int(r())

for _ in range(case):
  n, m = map(int, r().split())
  arr = list(map(int, r().split()))
  cnt = 0

  if len(arr) <= 1:
    print(1)
    continue

  while arr:
    biggest = True
    for j in range(1, len(arr)):
      if arr[0] < arr[j]:
        biggest = False
        break

    if biggest:
      arr.pop(0)
      cnt += 1

      if m == 0:
        print(cnt)
        break
      else:
        m -= 1
    else:
      arr.append(arr.pop(0))
      

      if m == 0:
        m = len(arr) - 1
      else:
        m -= 1