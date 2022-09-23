import sys
n = int(sys.stdin.readline().rstrip())

def solve(a, b, c):
    max_num = c.copy()
    max_num.sort()
    max_num.reverse()
    count = 0
    queue  =[]
    for i in range(a):
        queue.append([c[i], i])
    
    while queue:
        a = queue.pop(0)
        if a[0] == max_num[0]:
            if a[1]== b:
                break
            else:
                count += 1
                max_num.pop(0)
        else:
            queue.append(a)

    return count + 1


for _ in range(n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    c = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(a, b, c))