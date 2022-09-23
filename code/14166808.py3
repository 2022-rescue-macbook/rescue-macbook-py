import sys;
input = sys.stdin.readline;

T = int(input());
for t in range(T):
    n, m = map(int, input().split());
    importance = list(map(int ,input().split()));
    c = 0;
    while(True):
        if(max(importance) == importance[0]):
            c += 1;
            if(m == 0):
                break;
            importance = importance[1:];
            m -= 1;
        else:
            importance = importance[1:] + [importance[0]];
            if(m == 0):
                m = len(importance) - 1;
            else:
                m -= 1;
    print(c);

