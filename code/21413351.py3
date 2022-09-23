test_case=int(input())
for i in range(test_case):
	n, m = map(int, input().split())
	li = list(map(int, input().split()))
	target = [0 for _ in range(n)]
	target[m] = 1
	
	cnt = 0
	
	while True:
		if max(li) == li[0]:
			cnt+=1
			if target[0] == 1:
				print(cnt)
				break
			else:
				li.pop(0)
				target.pop(0)
		else:
			li.append(li.pop(0))
			target.append(target.pop(0))