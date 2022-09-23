Q = int(input())
for i in range(Q):
	N, index = map(int,input().split())
	queue = list(map(int,input().split()))
	count=0
	while True:
		if max(queue) == queue[0]:
			queue.pop(0)
			count+=1
			if index==0:print(count);break
			else:index-=1
		else:
			tmp = queue.pop(0)
			queue.append(tmp)
			if index==0:index=len(queue)-1
			else:index-=1