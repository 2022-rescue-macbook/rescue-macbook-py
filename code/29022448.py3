
def check(n, interest, rank):
    stack = []
    for i in range(n):
        stack.append([i, rank[i]])

    rank.sort()
    rank.reverse()

    answer = 0
    while True:
        if rank[0] > stack[0][1]:  # rank 비교
            stack.append(stack.pop(0))
        else:
            answer = answer + 1
            if stack[0][0] == interest:
                break
            else:
                rank.pop(0)
                stack.pop(0)

    print(answer)



n = int(input())

for _ in range(n):
    n, interest = list(map(int, input().split()))
    rank = list(map(int, input().split()))
    check(n,interest,rank)