from sys import stdin, stdout

for _ in range(int(stdin.readline())):
	n, m = map(int, stdin.readline().split())
	li = list(map(int, stdin.readline().split()))
	
	di = {}
	for e in li:
		if e in di:
			di[e] += 1
		else:
			di[e] = 1
	
	qu = 0
	finish = False
	
	maximum = max(di)
	
	while True:
		if finish:
			break
			
		for i in range(n):
			if li[i] == maximum:
				qu += 1
				
				if i == m:
					finish = True
					break
				
				di[li[i]] -= 1
				
				if di[li[i]] == 0:
					del di[maximum]
					maximum = max(di)
					
	stdout.write(str(qu) + "\n")
