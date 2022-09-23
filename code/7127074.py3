import sys

def operate(paperList, target=0):
  target_location = target
  count = 0
  while len(paperList) > 0:
    if paperList[0] >= max(paperList):
      paperList.pop(0)
      target_location -= 1
      count += 1
    else:
      paper = paperList.pop(0)
      paperList.append(paper)
      if target_location == 0:
        target_location = len(paperList) - 1
      else:
        target_location -= 1
    if target_location < 0 : break
  print(count)

for _ in range(int(sys.stdin.readline())):
  N, M = map(int, sys.stdin.readline().split())
  papers = list(map(int, sys.stdin.readline().split()))
  operate(papers, M)