n = int(input())
result = []

for _ in range(n):
    num, index = list(map(int, input().split(' ')))
    series = list(map(int, input().split(' ')))
    series_b = list(enumerate(series))
    i = 0
    while series:
        if series[0] != max(series):
            series.append(series.pop(0))
            series_b.append(series_b.pop(i))
        else:
            del(series[0])
            i += 1
            
    for i in range(len(series_b)):
        if series_b[i][0] == index:
            result.append(i+1)

for r in result:
    print(r)