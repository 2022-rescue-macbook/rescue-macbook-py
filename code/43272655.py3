def queue(list, count):
    while True:
        if list[0] < max(list):
            list.append(list[0])
            del list[0]
        elif list[0] == max(list) and list[0+1] == 0.1:
            count += 1
            return count
        else:
            count += 1
            del list[0]


f = int(input())
for _ in range(f):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(m+1, 0.1)
    count = 0
    print(queue(a, count))

