import sys
from collections.abc import Callable
from typing import Literal

from main import KthLargest


def trap[R](f: Callable[[], R]) -> R | Literal[False]:
    try:
        return f()
    except Exception:
        return False


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
