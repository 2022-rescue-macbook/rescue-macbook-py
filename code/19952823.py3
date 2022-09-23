class Queue:
  def __init__(self):
    self.data = []
 
  def size(self):
    return len(self.data)
 
  def isEmpty(self):
    return self.size() == 0
 
  def enqueue(self,item):
    self.data.append(item)
  
  def dequeue(self):
    if self.isEmpty():
      print('빈큐임')
    else:return self.data.pop(0)
 
  def peek(self):
    if self.isEmpty():
      print('빈큐임')
    else:
      return self.data[0]
 
n = int(input())
while n:
  l, ind = map(int, input().split())
  arr = list(map(int, input().split()))
  q = Queue()
  iq = Queue()
  for i in arr:
    q.enqueue(i)
  for i in range(l):
    iq.enqueue(i)
  ans = 0
  while True:
    p = q.dequeue()
    for i in q.data:
      if p < i:
        q.enqueue(p)
        iq.enqueue(iq.dequeue())
        break
    else: 
      ans += 1 
      if ind == iq.dequeue(): 
        break
  print(ans)
  n-=1
