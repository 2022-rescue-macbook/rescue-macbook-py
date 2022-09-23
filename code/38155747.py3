import sys
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n, m = map(int, sys.stdin.readline().split())
        qu = list(map(int, sys.stdin.readline().split()))
        out = 0
        while n:
            maxi = max(qu)
            current = qu.pop(0)
            if maxi > current:
                qu.append(current)
            else:
                out += 1
                n -= 1
                if m == 0:
                    break
            m = m - 1 if m > 0 else n - 1
        print(out)

main()