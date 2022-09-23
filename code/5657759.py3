for _ in range(int(input())):
	size, pos = map(int, input().split())
	qu = list(map(int, input().split()))
	num = 1
	while True:
		if max(qu) == qu[0]:
			if pos == 0:
				print(num)
				break
			else:
				num += 1
				pos -= 1
				del(qu[0])
		else:
			qu = qu[1:]+qu[0:1]
			pos -= 1
			if pos < 0:
				pos += len(qu)