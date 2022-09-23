import sys
read = lambda:sys.stdin.readline()
t = int(read())
while t:
	t -= 1
	n, m = map(int, read().split())
	li = list(map(int, read().split()))

	sli = sorted(li, reverse=True)
	task = 1
	while 1:
		if m == 0 and li[0] == sli[task - 1]:
			print(task)
			break
		elif li[0] == sli[task - 1]:
			task += 1
			li.pop(0)
			m -= 1
		else:
			li.append(li.pop(0))
			m -= 1
			if m < 0:m = len(li) - 1
