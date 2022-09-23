def has_bigger(l, p):
    for i in l:
        if i > p:
            return True
    return False

T = int(input())

for _ in range(T):
    N, I = [int(x) for x in input().split()]
    idx_q = list(range(N))
    prior_q = [int(x) for x in input().split()]
    print_q = []

    while not print_q or print_q[-1] != I:
        if has_bigger(prior_q, prior_q[0]):
            prior_q.append(prior_q.pop(0))
            idx_q.append(idx_q.pop(0))
        else:
            print_q.append(idx_q.pop(0))
            prior_q.pop(0)

    print(len(print_q))