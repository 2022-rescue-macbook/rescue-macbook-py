import sys

for i in range(int(sys.stdin.readline())):
	mass, vip = map(int, sys.stdin.readline().split())
	queue = list(map(int, sys.stdin.readline().split()))
	kill = 0

	while queue[vip] != -1:
		for k in range(len(queue)):
			if queue[vip] == -1:
				break
			elif queue[k] == max(queue):
				queue[k] = -1
				kill += 1
	print(kill)