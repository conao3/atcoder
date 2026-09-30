#!/usr/bin/env python3

YES = 'Yes'
NO = 'No'

def solve(N, M, parties):
    pass  # TODO: edit here

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
    print(solve(N, M, parties))

if __name__ == '__main__':
    main()
