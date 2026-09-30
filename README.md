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

To download sample cases, use online-judge-tools (`oj download`). It writes `test/sample-N.in` and `test/sample-N.out` in the current directory. Create the problem directory first, then run the command there. Replace the directory and the task URL for another problem.

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
