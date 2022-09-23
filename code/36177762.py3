from sys import stdin,stdout

def is_ok(arr_important):
	for i in range(1, len(arr_important)):
		if arr_important[i] > arr_important[0]:
			return False
	return True


for i in range(int(stdin.readline())):
	n, target_i = [*map(int,stdin.readline().split())]
	arr_important = [*map(int,stdin.readline().split())]

	nth = 0
	while target_i != -1:
		if is_ok(arr_important):
			del arr_important[0]
			nth+=1
		else:
			arr_important.append(arr_important.pop(0))
			if target_i == 0:
				target_i = len(arr_important)

		target_i -= 1
	stdout.write(str(nth)+"\n")