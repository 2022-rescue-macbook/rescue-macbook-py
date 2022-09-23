U=lambda:map(int,input().split())
for _ in range(int(input())):
 n,m=U();l,i,o=[*U()],m,0
 while 1:
  if l[0]==max(l):
   o+=1
   if i>0:del l[0];i-=1
   else:print(o);break
  else:
   if i>0:i-=1
   else:i=len(l)-1
   l.append(l.pop(0))