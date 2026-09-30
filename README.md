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
```

## Contests

| Contest | Problems |
|---------|----------|
| ABC121 | A, B, C, D |
| ABC139 | A, B, C, D, E, F |
| ABC156 | A, B, C, D, E, F |
| ABC208 | B |
| Code Festival 2016 Qual B | A, B, C, D, E |
| Sumitrust Bank Programming Contest 2019 | A, B, C, D, E, F |

## Requirements

- C++17 or later
- Python 3.6 or later

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

To download every problem in a contest, pass the contest id. The script reads the tasks page, creates `src/abc208_a/`, `src/abc208_b/`, and the rest, and saves samples under each `test/`.

```bash
scripts/prepare-contest.sh abc208
```

Upstream `oj-prepare` is the command that does this in one step. The current nixpkgs build does not start, because `pkg_resources` is gone, and its tasks-page parser does not accept the memory unit `MiB`. The script lists the task ids and calls `oj download` for each one.

To download a single problem, create the directory and run `oj download` there. It writes `test/sample-N.in` and `test/sample-N.out`.

```bash
mkdir -p src/abc208_b
cd src/abc208_b
nix run nixpkgs#online-judge-tools -- download https://atcoder.jp/contests/abc208/tasks/abc208_b
```

To test a Python solution against every sample in `test/`, stay in that directory and run:

```bash
nix run nixpkgs#online-judge-tools -- test -c 'python3 main.py'
```

## Author

conao3

## License

MIT
