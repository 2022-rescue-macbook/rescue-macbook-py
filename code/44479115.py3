
t = int(input())


def print_order():
    i = 0
    result = 0
    for j in range(9, 0, -1):
        for k in range(c[j]):
            while priorities[i] != j:
                i = (i + 1) % n

            priorities[i] = 0
            result += 1
            if m == i:
                return result
            
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    c = [0] * 10
    for p in priorities:
        c[p] += 1

    print(print_order())
