from sys import stdin

cnt = int(stdin.readline())

for _ in range(cnt):
  result = 1
  docCnt, idx = map(int, stdin.readline().split())
  priorQueue = stdin.readline().split()[0:docCnt]

  idxQueue = []
  for i in range(docCnt):
    idxQueue.append(i)
  
  while idxQueue:
    if priorQueue[0] < max(priorQueue):
      priorQueue.append(priorQueue[0])
      del priorQueue[0]
      idxQueue.append(idxQueue[0])
      del idxQueue[0]
    else:
      if idxQueue[0] == idx:
        print(result)
        break
      result += 1
      del priorQueue[0]
      del idxQueue[0]