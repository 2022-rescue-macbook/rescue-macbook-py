import sys
test = int(sys.stdin.readline())


for _ in range(test):
    n,m = map(int,sys.stdin.readline().split())

    queue = sys.stdin.readline().split()
    check = [0 for _ in range(n)]
    check[m] = 1
    count = 0
    while True:
        if queue[0] == max(queue):
            count += 1

            if check[0] != 1:
                del queue[0]
                del check[0]
            else:
                print(count)
                
                break
        else:
            queue.append(queue[0])
            check.append(check[0])
            del queue[0]
            del check[0]
