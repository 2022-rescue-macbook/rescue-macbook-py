import sys
import heapq

def checking_num(N, M):
	queue1 = []
	queue2 = []
	num_list = list(map(int, sys.stdin.readline().split()))
	for i in range(N):
		heapq.heappush(queue1, -num_list[i])
		if(i == M):
			save_priority = num_list[i]
		queue2.append((num_list[i], i))
	count = 1
	while(1):
		while(-queue1[0] != queue2[0][0]):
			queue2.append(queue2.pop(0))
		if(queue2[0][1] == M):
			break
		heapq.heappop(queue1)
		queue2.pop(0)
		count +=1

		
	return count

def main():
	test_case = int(input())
	for i in range(test_case):
		N, M = map(int, sys.stdin.readline().split())
		print(checking_num(N, M))
		
		
if __name__ == '__main__':
	main()
