#!/usr/bin/env python3

from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: int, A: int, B: int, S: str) -> List[str]:
def solve(N, A, B, S):
    pass


def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = solve(N, A, B, S)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
