import sys

def printQueue (m, values) :
	if len(values) == 1 : return 1
	
	count, seq = 0, [i for i in range(len(values))]
	while m in seq :
		temp = seq[0]
		for i in values[1:] : 
			if values[0] < i :
				values.append(values.pop(0))
				seq.append(seq.pop(0))
				break
		if temp == seq[0] :
			values.pop(0)
			seq.pop(0)
			count += 1
	return count

for _ in range(int(sys.stdin.readline())) :
	n, m = map(int, sys.stdin.readline().split())
	values = list(map(int, sys.stdin.readline().split()))[:n]
	print(printQueue(m, values))