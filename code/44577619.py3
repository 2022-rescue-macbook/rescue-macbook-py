for _ in range(int(input())):
    documents, query = list(map(int, input().split(' ')))
    affinities = list(map(int, input().split(' ')))
    affinity_table = {item: affinities.count(item) for item in set(affinities)}

    cursor, queue_idx = 0, 1
    for maxval in sorted(affinity_table.keys(), reverse=True):
        solved = False
        while affinity_table[maxval] > 0:
            if affinities[cursor] == maxval:
                if query == cursor:
                    solved = True
                    print(queue_idx)
                    break
                affinities[cursor] = 0
                queue_idx += 1
                affinity_table[maxval] -= 1
            cursor = (cursor + 1) % len(affinities)
        if solved: break