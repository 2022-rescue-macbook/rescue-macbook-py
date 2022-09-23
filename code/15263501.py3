from sys import stdin

data = stdin.read().split("\n")

data.pop(0)

for case in range(int(len(data)/2)):
    document = int(data.pop(0).split()[1])
    queue = data.pop(0).split()
    for i in range(len(queue)):
        queue[i] = (int(queue[i]), document == i)

    count = 1
    while True:
        current = queue.pop(0)

        if len(queue) == 0:
            print(count)
            break

        if current[0] != max(queue + [current])[0]:
            queue.append(current)
        elif not current[1]:
            count += 1
        else:
            print(count)
            break