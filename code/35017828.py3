qsize = 1001 #901도 충분
Q = [0] * qsize

f = e = 0
def reset():
    global f, e
    f = e = 0

def push(num):
    global e
    e += 1
    Q[e] = num

def popleft():
    global f
    f += 1
    return Q[f]

def isEmpty():
    global f, e
    if f == e:
        return True
    else:
        return False

for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    reset()
    important = [0] * 10
    for i, num in enumerate(nums):
        push((i, num))
        important[num] += 1

    for m in range(9, 0, -1):
        if important[m]:
            most_important = m
            break
    cnt = 0
    while not isEmpty():
        i, num = popleft()
        if num == most_important:
            cnt += 1
            if i == M:
                break
            important[num] -= 1
            if not important[num]:
                for m in range(num - 1, 0, -1):
                    if important[m]:
                        most_important = m
                        break
        else:
            push((i, num))
    
    print(cnt)
