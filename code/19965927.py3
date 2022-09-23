class ArrayQueue:
  def __init__(self):
    self.data = []
  
  def size(self):
    return len(self.data)

  def isEmpty(self):
    return self.size()==0

  def enqueue(self, item):
    self.data.append(item)

  def dequeue(self):
    if self.isEmpty():
      print("빈 큐임")
    else:
      return self.data.pop(0)

  def peek(self):
    if self.isEmpty():
      print("빈 큐임")
    else:
      return self.data[0]

#프린터 큐
num = int(input())
for i in range(num):
  n,m = map(int,input().split())
  arr = list(map(int,input().split()))
  ma = max(arr)
  q = ArrayQueue()
  index = 0
  for i in range(0,n):
    q.enqueue(i)
  while not q.isEmpty():
    tmp = q.dequeue()
    if arr[tmp] != ma :
      q.enqueue(tmp)
    else:
      index += 1
      arr[tmp] *= -1
      ma = max(arr)
      if tmp == m:
        break
  print(index)