n = int(input())

data1 = []
data2 = []
for i in range(n):
    data1.append(input())
    data2.append(input())

for j in range(n):
    N = int(data1[j].split(' ')[0])
    M = int(data1[j].split(' ')[1])
    priority = []
    for k in range(N):
        priority.append(int(data2[j].split(' ')[k]))
    p_index = list(range(N))
    v = 0
    while True:
        if priority[0] == max(priority):
            priority.pop(0)
            m = p_index.pop(0)
            v = v + 1
            if m == M:
                print(v)
                break
        else:
            priority.append(priority.pop(0))
            p_index.append(p_index.pop(0))