n = int(input())

result = []

for i in range(1, n + 1):
    cnt = 0
    priortyIdx = 0
    docs = []

    doc_cnt, target_pos = list(map(int, input().split()))
    priorties = list(map(int, input().split()))
    for doc_idx in range(0, doc_cnt):
        doc = {'is_target': False, 'priorty': 0}
        if doc_idx == target_pos:
            doc['is_target'] = True
        doc['priorty'] = priorties[doc_idx]
        docs.append(doc)

    priorties.sort(reverse=True)

    while len(docs) > 0:
        pop_target = docs.pop(0)
        if pop_target['priorty'] != priorties[0]:
            docs.append(pop_target)
            continue
        else:
            if pop_target['priorty'] == priorties[0]:
                priorties.pop(0)
                cnt += 1

            if pop_target['is_target'] == True:
                result.append(str(cnt))
                break

print('\n'.join(result))