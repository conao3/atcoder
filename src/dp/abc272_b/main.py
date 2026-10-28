#!/usr/bin/env python3

import itertools

YES = "Yes"
NO = "No"


def solve(N, M, parties) -> bool:
    combinations = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(M):
        for a, b in itertools.combinations(parties[i], 2):
            combinations[a][b] = True

    return sum(sum(row) for row in combinations) == N * (N - 1) / 2


def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    parties = []
    for _ in range(M):
        k = int(next(tokens))
        parties.append([int(next(tokens)) for _ in range(k)])
    assert next(tokens, None) is None
    print(YES if solve(N, M, parties) else NO)


if __name__ == "__main__":
    main()
