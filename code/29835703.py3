#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def solve(N, M, priorities):
    count = [0 for _ in range(10)]
    max_priority = 0
    for p in priorities:
        count[p] += 1
        if max_priority < p:
            max_priority = p

    docs = [(i, priorities[i]) for i in range(len(priorities))]
    order = 0
    while 0 < len(docs):
        doc = docs.pop(0)
        if doc[1] == max_priority:
            order += 1
            if doc[0] == M:
                return order
            count[max_priority] -= 1
            while count[max_priority] == 0 and 0 < max_priority:
                max_priority -= 1
        else:
            docs.append(doc)
    return -1


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        args = sys.stdin.readline().strip().split()
        N = int(args[0])
        M = int(args[1])
        priorities = [int(t) for t in sys.stdin.readline().strip().split()]

        print(solve(N, M, priorities))
