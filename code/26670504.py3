Test_Case = int(input())

result = list()

for i in range(Test_Case):
    N,M = list(map(int,input().split()))
    prior = list(map(int,input().split()))

    queue = list()
    loop =True

    while loop:
        if prior[0] == max(prior):
            queue.append(prior.pop(0))
            if M == 0:
                result.append(str(len(queue)))
                loop = False
                break
            else:
                M -= 1
        else:
            prior.append(prior.pop(0))
            if M == 0:
                M = len(prior) - 1
            else:
                M -= 1

print('\n'.join(result))