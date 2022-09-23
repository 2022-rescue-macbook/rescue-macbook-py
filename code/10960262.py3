class Queue():
  def __init__(self):
    self.list = []
    self.p_count = 0
  
  def enqueue(self, element):
    self.list.append(element)
  
  def dequeue(self):
    return self.list.pop(0)
  
  def empty(self):
    if len(self.list) == 0:
      return 0
    else:
      return 1

c = int(input())
ans = []
for i in range(c):
  que = Queue()
  seq = []
  N, M = map(int, input().split())
  
  val = list(map(int, input().split()))
  for j in range(N):
    que.enqueue([val[j], 0])
    seq.append(val[j])
  
  seq = sorted(seq)
  # 알고 싶은 M번째를 1로 만들어줌
  que.list[M][1] = 1
  
  while que.empty():
    val = que.dequeue()
    if val[0] != seq[-1]:
      que.enqueue(val)
    else:
      seq.pop()
      que.p_count +=1
      if val[1] == 1:
        ans.append(que.p_count)
      
for i in range(c):
  print(ans[i])
  
    