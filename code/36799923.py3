import sys
test = int(sys.stdin.readline())
for i in range(test) :
  n, m = map(int, sys.stdin.readline().split())
  q = list(map(int, sys.stdin.readline().split()))
  check = [True if i == m else False for i in range(n)]
  count = 0
  while True :
    max_idx = q.index(max(q))
    if check[max_idx] == True :
      print(count + 1)
      break
    else :
      q = q[max_idx + 1 :] + q[: max_idx]
      check = check[max_idx + 1 :] + check[: max_idx]
      count += 1