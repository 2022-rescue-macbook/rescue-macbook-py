tmp=int(input())
for i in range(tmp):
	n,m=map(int, input().split())
	arr=list(map(int,input().split()))
	check=[0 for i in range(n)]
	check[m]=1
	rank=0
	while True:
		if arr[0]==max(arr):
			rank+=1
			if check[0]==1:
				print(rank)
				break
			else:
				del check[0]
				del arr[0]
		else:
			arr.append(arr[0])
			check.append(check[0])
			del check[0]
			del arr[0]
