#!/usr/bin/env python3

from typing import *

MOD = 1000000007


# def solve(N: int, A: List[int]) -> int:
def solve(N, A):
    pass


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)


if __name__ == '__main__':
    main()
