T = int(input())
for i in range(0,T):
	info = list(map(int,input().split()))
	Queue = list(map(int,input().split()))
	Queue_ori = [0 for i in range(info[0])]
	for j in range(0,info[0]):
		Queue_ori[j] = [Queue[j],j]
	cnt = 0;
	while(True):
		if(max(Queue) == Queue[0]):
			cnt = cnt +1
			if(Queue_ori[0][1] == info[1]):
				print(cnt)
				break;
			else:
				del Queue[0]
				del Queue_ori[0]
		else:
			Queue.append(Queue[0])
			Queue_ori.append(Queue_ori[0])
			del Queue[0]
			del Queue_ori[0]
