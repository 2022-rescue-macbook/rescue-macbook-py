import sys


def solve(inp, idx):
    inp_ = [(inp[i], i == idx)for i in range(len(inp))]
    acc = 0
    while True:
        v, b = inp_.pop(0)
        can_print = True
        for v_, b_ in inp_:
            if v < v_:
                can_print = False
                break
        if can_print:
            acc += 1
            if b:
                print(acc)
                return
        else:
            inp_.append((v, b))


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        idx = int(sys.stdin.readline().strip().split()[1])
        inp = [int(c) for c in sys.stdin.readline().strip().split()]
        solve(inp, idx)
