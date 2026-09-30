#!/usr/bin/env python3

# def solve(H: int) -> int:
def solve(H):
    chain = []
    h = H
    while h:
        chain.append(h)
        h //= 2

    dp = {}
    for h in reversed(chain):
        if h == 1:
            dp[h] = 1
        else:
            dp[h] = 1 + 2 * dp[h // 2]

    return dp[H]

def main():
    H = int(input())
    a = solve(H)
    print(a)

if __name__ == '__main__':
    main()
