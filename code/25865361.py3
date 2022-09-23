test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split()))
    priority = list(map(int, input().split()))
    idx = list(range(len(priority)))
    idx[m] = 'target'  ## target 삽입시켜 놓기 

    # 순서
    order = 0
    i = 0

    while order != n:
        if priority[0]==max(priority):
            order += 1

            if idx[0]=='target':
                print(order)
                break
            else:
                priority.pop(0)
                idx.pop(0)

        else:
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))


