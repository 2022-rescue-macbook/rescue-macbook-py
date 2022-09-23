import sys
I = lambda : map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
  N,M = I();
  Q = list(I())
  Imp= Q[:]
  Imp.sort(reverse=True)

  Order = 0;
  while True:
    l = len(Q)
    front = Q.pop(0);

    if(front!=Imp[0]): 
      Q+=[front];
      M-=1
      M%=l
    else:
      Order +=1;
      if(M == 0): 
        print(Order)
        break;
      M-=1
      Imp.pop(0)