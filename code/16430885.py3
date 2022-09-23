import sys

T=int(sys.stdin.readline().strip())
answers=[]
for _ in range(T):

    N, I = map(int, sys.stdin.readline().strip().split(' '))
    value=list(map(int, sys.stdin.readline().strip().split(' ')))
    idxx=[i for i in range(N)]

    c=0

  

    while True:
        idx=idxx.pop(0)
        v=value.pop(0)
      

        if len(value)>0 and v < max(value):
            idxx.append(idx)
            value.append(v)
        else:
            c+=1
            if idx == I:
                answers.append(c)
                break
for i in answers:
    print(i)