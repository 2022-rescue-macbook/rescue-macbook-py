import sys
t = int(sys.stdin.readline())

for i in range(t):
	n,m = map(int,sys.stdin.readline().split())
	arr = list(map(int,sys.stdin.readline().split()))
	num = [0,0,0,0,0,0,0,0,0]
	arr[m] = arr[m] + 10
	for j in arr:
		if j > 10:
			num[j-11] = num[j-11] + 1
		else:
			num[j-1] = num[j-1] + 1
	count = 0
	while True:
		state = 0
		if arr[0] > 10:
			for j in range(arr[0]-10,9):
				if num[j] > 0:
					state = 1
					break
		else:
			for j in range(arr[0],9):
				if num[j] > 0:
					state = 1
					break
		if state == 0:
			if arr[0]>10:
				break
			count += 1
			num[arr[0]-1] = num[arr[0]-1] -1
			del arr[0]
		else:
			bucket = arr[0]
			del arr[0]
			arr.append(bucket)
	print(count+1)