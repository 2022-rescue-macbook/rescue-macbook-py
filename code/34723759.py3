t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	index_arr = list(range(len(arr)))
	target = index_arr[m]
	count = 0
	while 1:
		if arr[0] == max(arr):
			count += 1
			if index_arr[0] == target:
				print(count)
				break
			else:
				arr.pop(0)
				index_arr.pop(0)
		else:
			arr.append(arr.pop(0))
			index_arr.append(index_arr.pop(0))