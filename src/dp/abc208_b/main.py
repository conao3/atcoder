#!/usr/bin/env python3

import math
from typing import *


# def solve(N: int) -> int:
def solve(N):
    coins = 0
    for i in reversed(range(1, 11)):
        coin = math.factorial(i)
        take = N // coin
        coins += take
        N -= coin * take

    return coins


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == "__main__":
    main()
