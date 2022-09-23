T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    printer_q = list(map((lambda x : (int(x), False)), input().split()))
    printer_q[M] = (printer_q[M][0], True)
    
    stop = False
    sorted_q = []
    last_printed_index, last_printed_index_temp = 0, 0
    for i in range(9, 0, -1):
        for j in range(len(printer_q)):
            ind = (last_printed_index + j) % len(printer_q)
            val = printer_q[ind]
            if val[0] == i:
                sorted_q.append(val)
                last_printed_index_temp = ind
                if val[1]:
                    stop = True
                    break
        last_printed_index = last_printed_index_temp
        if stop:
            break
    print(len(sorted_q))