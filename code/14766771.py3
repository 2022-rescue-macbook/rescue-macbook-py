tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())

    words = list(map(int, input().split()))
    re = [i for i in range(1, n+1)]
    key = re[m]

    final = []
    while words:

        if words[0] >= max(words):
            num = words.pop(0)
            str_num = re.pop(0)
            final.append(str_num)
        else:
            num = words.pop(0)
            words.append(num)
            str_num = re.pop(0)
            re.append(str_num)

    print(final.index(key)+1)