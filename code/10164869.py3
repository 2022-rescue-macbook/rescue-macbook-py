import sys

def maxcheck(li):
	temp=li[0]
	for x in li:
		if temp<x:
			return False
	return True

def ft(target,priority):
	counter=0
	while target>=0:
		if maxcheck(priority)==True:
			if target==0:
				counter+=1
				break
			else:
				counter+=1
				target-=1
				priority.pop(0)
		else:
			if target==0:
				target=len(priority)-1
				priority.append(priority.pop(0))
			else:
				priority.append(priority.pop(0))
				target-=1
	return counter

num=int(sys.stdin.readline())
for _ in range(num):
	info=list(map(int,sys.stdin.readline().split()))
	target=info[1]
	priority=list(map(int,sys.stdin.readline().split()))
	print(ft(target,priority))