n = int(input())

for i in range(n):
  num, index= input().split()
  k = input().split()

  index = int(index)
  q = [int(i) for i in k]
  t = [int(i) for i in k]

  t.sort()
  place=1
  while q != []:
    if q[0]==t[-1]:
      if index==0:
        print(place)
        break
      else:
        index-=1
        q.pop(0)
        t.pop()
        place+=1
    else:   #중요도가 부족
      if index==0:
        index=len(q)-1
      else:
        index-=1
      q.append(q.pop(0))
      