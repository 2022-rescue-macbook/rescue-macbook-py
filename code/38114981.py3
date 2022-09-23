#프린터 큐
T=int(input())
answers=[]
for i in range(T):
  N, M = map(int,input().split(" "))
  docs = list(map(int,input().split(" ")))
  docs_sorted=list(docs)
  docs_sorted.sort()
  target=docs[M]
  p=0
  print_cnt=0
  while(True) :
    if docs[p]>=docs_sorted[-1]:
      docs_sorted.pop()
      print_cnt+=1
      if p==M:
        break
    else:
      docs.append(docs[p])
      if p==M:
        M=len(docs)-1
    p+=1
  answers.append(print_cnt)

for c in answers:
  print(c)

