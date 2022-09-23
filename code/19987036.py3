case = int(input())

for _ in range(case):
  N, M = map(int, input().split())
  print_list = list(map(int, input().split()))
  prior_number = []

  #우선 순위를 탐색하기 위한 리스트
  for doc in print_list:
    prior_number.append(doc)

  #큐 안에 index를 넣어 탐색
  result = [0 for _ in range(N)]
  queue = [ i for i in range(N)]
  seq = 1
  while queue:
    if print_list[queue[0]] == max(prior_number):
      prior_number.remove(max(prior_number))
      result[queue.pop(0)] = seq
      seq += 1
    else:
      queue.append(queue.pop(0))
  print(result[M])  