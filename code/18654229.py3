def func1(n, m):
    if n < 1 or n > 100:
        exit()
    if m < 0 or m >= n:
        exit()

def func2(n, m, imp):
    func1(n, m)
    imp_list = imp.split(' ')
    important = []
    loc = m
    if n == len(imp_list):
        for i in imp_list:
            important.append(int(i))
    else:
        exit()
    cnt = 0
    while len(important) != 0:
        exist = False
        for i in range(1, n):
            if important[0] < important[i]:
                tmp = important.pop(0)
                important.append(tmp)
                exist = True
                if loc == 0:
                    loc = n - 1
                else:
                    loc -= 1
                break
        if exist == False:
            tmp = important.pop(0)
            cnt += 1
            n -= 1
            if loc == 0:
                break
            else:
                loc -= 1
    return cnt

if __name__ == "__main__":
    t = int(input())
    result = []
    for i in range(t):
        n, m = map(int, input().split())
        imp = input()
        result.append(func2(n, m, imp))
    for i in result:
        print(i)