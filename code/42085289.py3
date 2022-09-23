import sys
input=sys.stdin.readline

N=int(input())
for _ in range(N):
  List_N=list(map(int,input().split(" ")))
  List_M=list(map(int,input().split(" ")))
  k=List_N[1]
  List=list(List_M)
  List[k]=0
  answer=0
  while True:
    if List_M[0]==max(List_M):
      answer+=1
      if List[0]==0:
        print(answer)
        break
      else:
        List_M.pop(0)
        List.pop(0)
    else:
      List_M.append(List_M.pop(0))
      List.append(List.pop(0))