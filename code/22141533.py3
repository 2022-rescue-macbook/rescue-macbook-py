loop = int(input())

def solve(m, docs):
    index = m
    count = 0
    list = docs

    while True:
        if list[0] < max(list):
            list.append(list[0])
            del list[0]
            if index == 0:
                index = len(list) -1
            else:
                index -=1
        else:
            del list[0]
            count+=1
            if index == 0:
                break
            else:
                index -=1
    return count


answer = []

for i in range(loop):
    m = list(map(int, input().split(' ')))[1]
    docs = list(map(int, input().split(' ')))
    answer.append(solve(m, docs))

for a in answer:
    print(a)