import sys
for _ in range(int(input())):
	N,M=map(int,input().split())
	m,c,Q=0,0,[]
	for i,j in enumerate(map(int,sys.stdin.readline().split())):
		if m<j:m=j
		if i==M:Q.append([j,1])
		else:Q.append([j,0])
	while(True):
		if Q[0][0]<m:
			Q.append(Q.pop(0))
		elif Q[0][0]==m:
			c+=1
			if Q[0][1]==1:break
			m=0
			Q.pop(0)
			for p in Q:
				if m<p[0]:m=p[0]
	print(c)