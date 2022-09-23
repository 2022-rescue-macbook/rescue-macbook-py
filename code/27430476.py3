num_case = int(input())
for _ in range(num_case):
    num_docs, target_index = map(int, input().split())
    priorities = list(map(int, input().split()))
    docs = [i for i in range(num_docs)]
    count = 1
    while True:
        max_prior = max(priorities)
        max_index = priorities.index(max_prior)
        priorities = [*priorities[max_index+1:], *priorities[:max_index]]
        if docs[max_index] == target_index:
            print(count)
            break
        else:
            docs = [*docs[max_index+1:], *docs[:max_index]]
            count += 1