#!/usr/bin/env python3



# def solve(N: int, P: List[int]) -> int:
def solve(N, P):
    dp = [-1 for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        p = P[i - 1]
        dp[i] = dp[p - 1] + 1

    return dp[N - 1]

def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = [None for _ in range(N - 1)]
    for i in range(N - 1):
        P[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P)
    print(a)

if __name__ == '__main__':
    main()
