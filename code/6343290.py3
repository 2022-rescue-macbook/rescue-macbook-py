for _ in range(int(input())):
 r=t=i=0;n,k=map(int,input().split());a=[*map(int,input().split())];b=sorted(a)
 while b:f=a[i]==b[-1]==b.pop();t+=f;r+=f*t*(i==k);i=-~i%n
 print(r)