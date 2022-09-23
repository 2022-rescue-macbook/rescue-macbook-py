import sys
if __name__ == "__main__":
   t = int(sys.stdin.readline())

   for _ in range(t):
      n, m = map(int, sys.stdin.readline().rstrip().split())
      jobs = list(map(int, sys.stdin.readline().rstrip().split()))
      mine = jobs[m]
      cost = 1
      while 1:
         max_i = jobs.index(max(jobs))
         if m == max_i:
            print(cost)
            break
         jobs = jobs[max_i+1:] + jobs[:max_i]
         m = m-(max_i+1) if m>max_i else m+(len(jobs)-max_i)
         cost += 1