import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
	n, m = map(int, input().split())
	weight = list(map(int, input().split()))
	idx = [i for i in range(n)]
	result = 0

	while weight :
		if max(weight) != weight[0] :
			weight.append(weight.pop(0))
			idx.append(idx.pop(0))
		else :
			result += 1
			if idx[0] == m :
				print(result)
				break
			weight.pop(0)
			idx.pop(0)