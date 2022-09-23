for i in range(int(input())) :
    n, x = map(int, input().split())
    important = list(map(int, input().split()))

    files = [chr(i) for i in range(65, 65 + n)]
    target = files[x]
    answer = []

    for j in range(n) :
        temp = important.index(max(important))
        answer.append(files[temp])
        files = files[temp + 1:] + files[:temp]
        important = important[temp + 1:] + important[:temp]

    print(answer.index(target) + 1)