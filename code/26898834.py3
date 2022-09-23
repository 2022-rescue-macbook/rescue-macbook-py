import sys
input = sys.stdin.readline
t = int(input())
result = ""

for _ in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    queue = [i for i in range(n)]
    maximum = max(prior)
    answer = 1
    
    while(queue):
        if maximum > prior[0]:
            prior.append(prior[0])
            prior = prior[1:]
            queue.append(queue[0])
            queue = queue[1:]
        else:
            if queue[0] == m:
                result += str(answer)+"\n"
                break
            else:
                prior = prior[1:]
                queue = queue[1:]
                maximum = max(prior)
                answer += 1
print(result)