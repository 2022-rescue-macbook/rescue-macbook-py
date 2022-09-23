case = int(input())

for i in range(case):
    count = 0
    many, posit = map(int, input().split())
    impo = input().split()

    tag = impo[posit]+'t'
    impo[posit] = tag
    while tag in impo:
        if impo[0][0] == max(impo)[0]:
            del impo[0]
            count += 1
        else:
            impo.append(impo.pop(0))

    print(count)
