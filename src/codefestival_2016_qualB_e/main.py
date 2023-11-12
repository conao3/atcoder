#!/usr/bin/env python3

from typing import *


# def solve(a: int, b: List[str], c: int, d: List[int], e: List[str]) -> List[str]:
def solve(a, b, c, d, e):
    pass


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = int(next(tokens))
    b = [None for _ in range(a)]
    for i in range(a):
        b[i] = next(tokens)
    c = int(next(tokens))
    d = [None for _ in range(c)]
    e = [None for _ in range(c)]
    for i in range(c):
        d[i] = int(next(tokens))
        e[i] = next(tokens)
    assert next(tokens, None) is None
    f = solve(a, b, c, d, e)
    for i in range(c):
        print(f[i])


if __name__ == '__main__':
    main()
