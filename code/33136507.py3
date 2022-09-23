t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  docs = list(map(int, input().split()))
  orderArr = []
  for j in range(n):
    orderArr.append(j)
  
  cnt = 1
  while len(docs) != 0:
    
    # print(cnt, docs)
    if max(docs) == docs[0]:
      if orderArr[0] == m:
        print(cnt)
        break
      else:
        docs.pop(0)
        orderArr.pop(0)
        cnt += 1
    else:
      docs.append(docs.pop(0))
      orderArr.append(orderArr.pop(0))