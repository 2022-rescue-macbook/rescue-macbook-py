import sys

tc = int(sys.stdin.readline())



for _ in range(tc):
    n, m = list(map(int, sys.stdin.readline().split()))
    priority = list(map(int, sys.stdin.readline().split()))
    target = list(range(len(priority)))
    target[m] = "target"
    idx = 0

    while True:
        if(priority[0] == max(priority)):
            idx += 1
    
            if(target[0] == "target"):
                sys.stdout.write(str(idx) + '\n')
                break
            else:
                target.pop(0)
                priority.pop(0)
        else:
            target.append(target.pop(0))
            priority.append(priority.pop(0))