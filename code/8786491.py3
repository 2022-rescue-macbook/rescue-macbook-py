import sys

T = int(sys.stdin.readline().replace('\n', ''))

for i in range(T):
    N, M = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
    print_q = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
    priorities = sorted(print_q.copy(), key=lambda x: -x)
    target_priority = print_q[M]
    target_index = [False for i in range(N)]
    target_index[M] = True

    count = 0
    while True:
        if print_q[0] == priorities[0]:
            count += 1
            if target_index[0] == True:
                print(count)
                break
            print_q.pop(0)
            priorities.pop(0)
            target_index.pop(0)
        else:
            print_q.append(print_q.pop(0))
            target_index.append(target_index.pop(0))