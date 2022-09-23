cases = int(input())

for i in range(cases):
    jobs, target = list(map(int, input().split(' ')))
    priority_list = list(map(int, input().split(' ')))

    job_tuple_list = [(k, priority_list[k]) for k in range(jobs)]
    target_job = job_tuple_list[target][0]
    priority_sorted = sorted(priority_list)

    count = 0
    while job_tuple_list:
        count = count + 1
        max_priority = priority_sorted.pop()
        while job_tuple_list[0][1] != max_priority:
            job_tuple_list.append(job_tuple_list.pop(0))

        printed = job_tuple_list.pop(0)[0]
        if printed == target_job:
            break

    print(count)
