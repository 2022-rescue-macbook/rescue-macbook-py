t = int(input())

def check_q(q):
    answer = 0
    while True:
        doc = q.pop(0)
        for prio, _ in q:
            if doc[0] < prio:
                q.append(doc)
                break
        else:
            answer += 1
            if doc[1]:
                print(answer)
                return

for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(lambda x: [int(x), False], input().split()))
    q[m][1] = True
    check_q(q)