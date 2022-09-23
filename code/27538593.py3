def solution(n, m, priorities):
    order = sorted(priorities, reverse=True)
    p = priorities*n

    stack = []

    ord_idx = 0
    cnt = 0

    answer = -1

    for i in range(len(p)):
        if order[ord_idx] == p[i]:
            real_idx = i % n
            stack.append(real_idx)
            ord_idx += 1
            cnt += 1
            if real_idx == m:
                answer = cnt
                break
    return answer


test_cases = []
t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    priorities = list(map(int, input().strip().split()))
    test_cases.append([n, m, priorities])

for test_case in test_cases:
    print(solution(*test_case))