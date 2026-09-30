#!/usr/bin/env bash
# Download every problem in an AtCoder contest into src/{problem_id}/test/.
# Usage: scripts/prepare-contest.sh abc208
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/prepare-contest.sh abc208" >&2
  exit 2
fi

contest=$1
if [[ $contest == http://* || $contest == https://* ]]; then
  contest=${contest%/}
  contest=${contest##*/}
fi

root=$(cd "$(dirname "$0")/.." && pwd)
tasks_url="https://atcoder.jp/contests/${contest}/tasks"
html=$(curl -fsSL -A 'online-judge-tools' "$tasks_url")

mapfile -t problems < <(printf '%s' "$html" | python3 -c '
import re
import sys

contest = sys.argv[1]
html = sys.stdin.read()
seen = []
for problem_id in re.findall(r"/contests/" + re.escape(contest) + r"/tasks/([A-Za-z0-9_]+)", html):
    if problem_id not in seen:
        seen.append(problem_id)
if not seen:
    sys.exit(1)
print("\n".join(seen))
' "$contest")

echo "contest ${contest}: ${#problems[@]} problems"
nix shell nixpkgs#online-judge-tools --command bash -s -- "$root" "$contest" "${problems[@]}" << 'EOF'
set -euo pipefail
root=$1
contest=$2
shift 2
for problem_id in "$@"; do
  dir="${root}/src/${problem_id}"
  mkdir -p "$dir"
  echo "download ${problem_id} -> src/${problem_id}/test"
  (
    cd "$dir"
    oj download "https://atcoder.jp/contests/${contest}/tasks/${problem_id}"
  )
done
EOF
