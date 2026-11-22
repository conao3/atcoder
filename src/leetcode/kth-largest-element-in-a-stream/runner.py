import sys

from main import KthLargest

for names_line in sys.stdin:
    args_line = next(sys.stdin, None)
    if args_line is None:
        break
    names = eval(names_line)
    args = eval(args_line)
    sol: list[int | None] = [
        None,
    ]
    obj = KthLargest(*args[0])
    print(f"line: {args}")
    for [i] in args[1:]:
        sol.append(obj.add(i))
    print(str(sol).replace(" ", ""))
