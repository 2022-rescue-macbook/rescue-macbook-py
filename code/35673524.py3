N = int(input())

test_cases = list()
seq_lists = list()

for i in range(N):
  test_case = list(map(int, input().split()))
  seq_list = list(map(int, input().split()))
  test_cases.append(test_case)
  seq_lists.append(seq_list)

def solve(test_case, seq_list):
  queue = seq_list
  tmp_max = max(seq_list)
  cnt = 1
  curr_idx = test_case[1]

  while seq_list:
    if seq_list[0] == tmp_max:
      seq_list.pop(0)
      if curr_idx == 0:
        return cnt
      cnt += 1
      curr_idx -= 1
      tmp_max = max(seq_list)

    else:
      tmp = seq_list.pop(0)
      seq_list.append(tmp)
      if curr_idx != 0:
        curr_idx -= 1
      else:
        curr_idx = len(seq_list)-1


for i in range(N):
  print(solve(test_cases[i], seq_lists[i]))





