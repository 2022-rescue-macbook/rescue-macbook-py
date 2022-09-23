from sys import stdin, stdout
TC = int(stdin.readline())

for _ in range(TC):
	n, m = map(int, stdin.readline().split())

	a = list(map(int,stdin.readline().split()))
	idx = 0
	target_arr = [False for _ in range(n)]
	target_arr[m] = True

	while True:
		if a[0] == max(a):
			idx += 1
			if target_arr[0] == True:
				print(idx)
				break
			else:
				a.pop(0)
				target_arr.pop(0)
		else:
			a.append(a.pop(0))
			target_arr.append(target_arr.pop(0))        
