import sys


def queue_max(queue):
	result = 0
	for i in range(len(queue)):
		if queue[i][1] > result:
			result = queue[i][1]

	return result		


if __name__ == '__main__':
	input = sys.stdin.readline
	test_cases = int(input())

	for i in range(test_cases):
		N, M = map(int ,input().split())
		# if N == 1:
		# 	print(1)
		l = input().split()
		queue = []
		for j in range(N):
			queue.append((j, int(l[j])))

		# print(queue)
		
		i = 1
		max_0 = queue_max(queue)
		# print(max_0)
		while queue[0][1] != max_0 or  queue[0][0] != M:
			
			a = queue.pop(0)
			if a[1] == max_0:
				max_0 = queue_max(queue)
				i += 1
			else: queue.append(a)

			# print(queue)




		print(i)