iter = int(input())
result = []
for _ in range(iter):
    num_doc, location = map(int, input().split(" "))
    scores = list(map(int, input().split(" ")))

    check = []
    for i in range(len(scores)):
        if i == location:
            check.append(1)
        else:
            check.append(0)

    flag = True
    cnt = 0
    while flag:
        if scores[0] >= max(scores):
            cnt += 1
            if check[0] == 1:
                result.append(cnt)
                flag = False
            scores.pop(0)
            check.pop(0)
        else:
            score = scores.pop(0)
            c = check.pop(0)
            scores.append(score)
            check.append(c)

for i in result:
    print(i)