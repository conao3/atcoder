#!/usr/bin/env python3

from typing import *


# def solve(k: int, q: int, d: List[int], n: List[int], x: List[int], m: List[int]) -> List[str]:
def solve(k, q, d, n, x, m):
    pass


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    k = int(next(tokens))
    q = int(next(tokens))
    d = [None for _ in range(k)]
    n = [None for _ in range(q)]
    x = [None for _ in range(q)]
    m = [None for _ in range(q)]
    for i in range(k):
        d[i] = int(next(tokens))
    for i in range(q):
        n[i] = int(next(tokens))
        x[i] = int(next(tokens))
        m[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(k, q, d, n, x, m)
    for i in range(q):
        print(a[i])


if __name__ == '__main__':
    main()
