import sys

N = int(sys.stdin.readline())


for _ in range (N):
  N, M = map(int,sys.stdin.readline().split())
  data_k = list(map(int, sys.stdin.readline().split()))
  count = 0

  data = []

  for i in range(len(data_k)):
    data.append([data_k[i],i])

  a = max(data)

  a = data[data.index(a)][0]

  answer=[]

  while True:
    if data[0][0]==a:
      b = data[0]
      answer.append(b)
      data.remove(data[0])
      if len(data)==0:
        break
      else:
        a = data[data.index(max(data))][0]
    else:
      c = data[0]
      data.append(c)
      data.remove(data[0])

  for i in range (len(answer)):
    if answer[i][1]==M:
      print(i+1)
      break
  




