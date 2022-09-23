import sys

test_case = int(input())
for _ in range(test_case):
    N, target = map(int,sys.stdin.readline().split())
    queue = []
    temp = map(int,sys.stdin.readline().split())
    for i , ele in enumerate(temp):
        queue.append((ele,i))
    count = 0
    while queue :
        front , number = queue.pop(0)            
        for ele,i in queue:
            if ele > front :
                queue.append((front,number))
                break
        else:
            count +=1
            if number == target:
                break
    print(count)