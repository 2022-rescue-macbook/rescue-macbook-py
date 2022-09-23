for _ in range(int(input())):
	n, m = map(int, input().split())
	items = map(int, input().split())
	l = [(item, i) for i, item in enumerate(items)]

	cnt = 1
	while True:
		doc, idx = l.pop(0)

		if any(d > doc for d, i in l):
			l.append((doc, idx))
		else:
			if idx == m:
				print(cnt)
				break
			else:
				cnt += 1

