#!/usr/bin/env python3

from typing import *


# def solve(n: int, a: List[int], b: List[int]) -> float:
def solve(n, a, b):
    pass


def main():
    n = int(input())
    a = [None for _ in range(n)]
    b = [None for _ in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a1 = solve(n, a, b)
    print(a1)


if __name__ == '__main__':
    main()
