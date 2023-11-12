#!/usr/bin/env python3

from typing import *


# def solve(N: int, A: List[int]) -> int:
def solve(N, A):
    pass


def main():
    N = int(input())
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
    a = solve(N, A)
    print(a)


if __name__ == '__main__':
    main()
