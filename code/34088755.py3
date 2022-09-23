import sys

input = sys.stdin.readline

def inputData():
	T = int(input())
	for _ in range(T):
		n,m = [int(i) for i in input().split(" ")]
		docs = [int(i) for i in input().split(" ")]
		maxValue = max(docs)
		printer(docs,m,maxValue)

def printer(docs,m,maxValue):
	arr = makeOrderQueue(docs,maxValue)
	cnt = 1
	for i in arr:
		if i[1] == m:
			break
		cnt += 1
	print(cnt)
	
def makeOrderQueue(docs,maxValue):
	printerOrder = []
	queue = []
	for i in range(len(docs)):
		queue.append((docs[i],i))
	count = 0
	while queue:
		a = queue[0]
		if maxValue > a[0]:
			tmp = queue.pop(0)
			queue.append(tmp)
		elif maxValue == a[0]:
			printerOrder.append(queue[0])
			queue.pop(0)
			if queue:
				maxValue = max(queue)[0]
	return printerOrder
inputData()