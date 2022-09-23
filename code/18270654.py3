case = eval(input())
t = []
for i in range(case):
  k = list(map(int,input().split()))
  arr = list(map(int,input().split()))
  c = 0
  want = k[1]
  
  while not want == -1:
    v = max(arr)
    if arr[0] == v:
      arr.pop(0)
      c += 1
      if want == 0:
        want = -1
      else :
        want -= 1
    else :
      arr.append(arr.pop(0))
      if want == 0:
        want = len(arr) -1
      else :
        want -= 1
  t.append(c)

for i in t :
  print(i)