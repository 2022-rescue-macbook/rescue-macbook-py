import sys
def printer():
    reps = int(sys.stdin.readline().rstrip())
    
    for _ in range(reps):
        n, m = map(int, sys.stdin.readline().split())
        priority = list(map(int, sys.stdin.readline().split()))
        chosen = [None] * n
        chosen[m] = "goal"
        cnt = 0
        while True:
            if priority[0] == max(priority):
                cnt += 1
                priority.pop(0)
                goal = chosen.pop(0)
                if goal == "goal":
                    print(cnt)
                    break
            else:
                priority.append(priority.pop(0))
                chosen.append(chosen.pop(0))

printer()