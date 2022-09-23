case = int(input())
result = []

for i in range(0, case):
    count = 0
    n, m = map(int, input().split(' '))
    pop = list(map(int, input().split(' ')))
    while pop[m] != 0:
        if pop[count] == max(pop):
            pop[count] = 0
            if pop[m] == 0:
                # print(pop.count(0))
                print(pop.count(0))
                break

        count += 1
        if count >= len(pop):
            count = 0
