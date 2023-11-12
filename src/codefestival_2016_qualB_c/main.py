#!/usr/bin/env python3

from typing import *


# def solve(W: int, H: int, p: List[int], q: List[int]) -> int:
def solve(W, H, p, q):
    pass


def main():
    W, H = map(int, input().split())
    p = [None for _ in range(W)]
    q = [None for _ in range(H)]
    for i in range(W):
        p[i] = int(input())
    for i in range(H):
        q[i] = int(input())
    a = solve(W, H, p, q)
    print(a)


if __name__ == '__main__':
    main()
