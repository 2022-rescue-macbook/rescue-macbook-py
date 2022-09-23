from collections import deque
import sys

def main():
	t = int(sys.stdin.readline())
	for _ in range(t):
		n, m = map(int, sys.stdin.readline().split())
		arr = list(map(int, sys.stdin.readline().split()))

		queues = [[] for _ in range(10)]
		if (n == 1):
			print(1)
			continue

		curr = 0
		start = curr
		stop = 0
		for i in range(9, 0, -1):
			curr = start
			if (arr[curr] == i):
				queues[i].append(curr)
				stop = curr
			curr = (start+1)%n
			while (curr != (start)%n):
				if (arr[curr] == i):
					queues[i].append(curr)
					stop = curr
				curr = (curr+1)%n
			start = stop

		idx = arr[m]
		res = 0
		for i in range(9, idx, -1):
			res += len(queues[i])
		for el in queues[idx]:
			res += 1
			if (el == m):
				break
		print(res)
			

main()
