import sys
input = sys.stdin.readline
for _ in range(int(input())):
    file, idx = map(int, input().split())
    weight = list(map(int, input().split()))
	
    cnt = 0
    pop = 0
    while weight:
	    if weight[cnt] == max(weight[cnt:]):
	        pop += 1
	        if cnt == idx:
	            print(pop)
	            break
	        cnt += 1
	    else:
	        if cnt == idx:
	            idx += len(weight) - cnt
	        weight.append(weight[cnt])
	        cnt += 1