import sys

t = int(input())
for i in range(t):
	res = 0
	n, m = map(int, sys.stdin.readline().split())
	arr = list(map(int, sys.stdin.readline().split()))
	arr_copy = list(range(len(arr)))
	arr_copy[m] = 'find'
	while arr:
		max_value = max(arr)
		while arr[0] != max_value:
			arr.append(arr.pop(0))
			arr_copy.append(arr_copy.pop(0))
		arr.pop(0)
		tmp = arr_copy.pop(0)
		res += 1
		if tmp == 'find':
			print(res)
			break