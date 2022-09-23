import sys
T=int(sys.stdin.readline())

for _ in range(T):
	N, flag = map(int,sys.stdin.readline().split())
	printer = list(map(int,sys.stdin.readline().split()))
	idx = list(range(N))
	order = 0
	while 1:
		if max(printer) == printer[0]:
			order += 1
			if flag == idx[0]:
				print(order)
				break
			else:
				printer.pop(0)
				idx.pop(0)
		else:
			printer.append(printer.pop(0))
			idx.append(idx.pop(0))