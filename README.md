# AtCoder Solutions

My solutions for AtCoder competitive programming problems, written in C++ and Python.

## Repository Structure

```
src/
  {contest}_{problem}/
    main.cpp       # C++ solution
    main.py        # Python solution
    generate.py    # Test case generator
    test/          # Sample test cases
  dp/
    {contest}_{problem}/
      main.py      # DP practice
      test/
```

## Contests

| Contest | Problems |
|---------|----------|
| ABC121 | A, B, C, D |
| ABC139 | A, B, C, D, E, F |
| ABC156 | A, B, C, D, E, F |
| ABC208 | A, C, D, E, F |
| Code Festival 2016 Qual B | A, B, C, D, E |
| Sumitrust Bank Programming Contest 2019 | A, B, C, D, E, F |

## DP

DP practice lives under `src/dp/`.

| Problem | Path |
|---|---|
| ABC208 B | `src/dp/abc208_b` |
| ABC153 D | `src/dp/abc153_d` |

## Requirements

- C++17 or later
- Python 3.6 or later

## Complexity

AtCoder's Python course says the judge runs about 10^8 to 10^9 operations per second ([EX19](https://atcoder.jp/contests/apg4bPython/tasks/APG4bPython_cd)). That figure is the C++ scale. For C++ and a 1 second limit, プログラミングコンテストチャレンジブック gives 10^7 iterations as likely to pass, and 10^8 as passing only when each step is very simple.

With a 2 second limit read as about 10^8 simple steps, the usual match between the constraint and the algorithm is:

| Maximum N | Order that fits |
|---|---|
| 10^2 | O(N^3) |
| 10^3 to 10^4 | O(N^2) |
| 10^5 to 10^6 | O(N log N) |
| 10^7 to 10^8 | O(N) |
| 10^9 and above | O(log N) or O(1) |

PyPy on AtCoder is about one digit tighter. A 2021 measurement with a 2 second limit ran a loop of 10^7 assignments in 487 ms, and a loop of 10^8 timed out ([RIT Tech Blog](https://rit-inc.hatenablog.com/entry/2021/12/13/180125)). Treat 10^7 as the PyPy budget. The same course notes that a program which passes in PyPy can still time out in CPython.

ABC208 B has a 2 second limit and N ≤ 10^7. A DP that tries every coin type at every amount is about 10 kinds × 10^7 = 10^8 updates, the size that timed out above. The greedy pass is 10 divisions.

## Usage

To compile and run a C++ solution:

```bash
cd src/abc121_a
g++ -std=c++17 -O2 main.cpp -o solution
./solution < test/sample-1.in
```

To run a Python solution:

```bash
cd src/abc121_a
python3 main.py < test/sample-1.in
```

To download every problem in a contest, pass the contest id. The script reads the tasks page and, for each task not already saved, creates `src/{problem_id}/` and saves samples under `test/`. A problem whose `test/sample-1.in` is already present under `src/{problem_id}/` or `src/dp/{problem_id}/` is skipped, so running the script again continues with the remaining problems.

```bash
scripts/prepare-contest.sh abc208
scripts/prepare-contest.sh https://atcoder.jp/contests/abc153/tasks/abc153_d --folder dp
```

A contest id or a contest URL downloads every task into `src/{problem_id}/`. A task URL downloads that task only. `--folder dp` puts the directory under `src/dp/` instead, so the command above creates `src/dp/abc153_d/`.

Upstream `oj-prepare` is the command that does this in one step. The current nixpkgs build does not start, because `pkg_resources` is gone, and its tasks-page parser does not accept the memory unit `MiB`. The script lists the task ids and calls `oj download` for each one.

To download a single problem, create the directory and run `oj download` there. It writes `test/sample-N.in` and `test/sample-N.out`.

```bash
mkdir -p src/abc208_a
cd src/abc208_a
nix run nixpkgs#online-judge-tools -- download https://atcoder.jp/contests/abc208/tasks/abc208_a
```

To test a Python solution against every sample in `test/`, stay in that directory and run:

```bash
nix run nixpkgs#online-judge-tools -- test -c 'python3 main.py'
```

## Author

conao3

## License

MIT
