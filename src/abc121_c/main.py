#!/usr/bin/env python3

from typing import *


# def solve(N: int, M: int, A: List[int], B: List[int]) -> int:
def solve(N, M, A, B):
    pass


def main():
    N, M = map(int, input().split())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    a = solve(N, M, A, B)
    print(a)


if __name__ == '__main__':
    main()
