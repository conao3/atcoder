#!/usr/bin/env python3

from typing import *


# def solve(a: str, b: str, c: List[str], d: List[List[str]], e: str) -> int:
def solve(a, b, c, d, e):
    pass


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = next(tokens)
    c = [None for _ in range(a)]
    d = [[None for _ in range(a)] for _ in range(a)]
    b = next(tokens)
    for i in range(a):
        c[i] = next(tokens)
        for j in range(i):
            d[i][j] = next(tokens)
    e = next(tokens)
    assert next(tokens, None) is None
    a1 = solve(a, b, c, d, e)
    print(a1)


if __name__ == '__main__':
    main()
