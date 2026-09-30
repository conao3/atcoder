#!/usr/bin/env bash
# Download AtCoder samples.
# Usage:
#   scripts/prepare-contest.sh abc208
#   scripts/prepare-contest.sh https://atcoder.jp/contests/abc153/tasks/abc153_d --folder dp
set -euo pipefail

usage() {
  echo "usage: scripts/prepare-contest.sh abc208" >&2
  echo "       scripts/prepare-contest.sh https://atcoder.jp/contests/abc153/tasks/abc153_d --folder dp" >&2
  exit 2
}

folder=src
target=
while [[ $# -gt 0 ]]; do
  case "$1" in
    --folder)
      [[ $# -ge 2 ]] || usage
      folder=$2
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    *)
      [[ -z "$target" ]] || usage
      target=$1
      shift
      ;;
  esac
done
[[ -n "$target" ]] || usage
if [[ ! "$folder" =~ ^[A-Za-z0-9_-]+$ ]]; then
  echo "folder must be a single directory name" >&2
  exit 2
fi
if [[ "$folder" != src ]]; then
  folder="src/${folder}"
fi

target=${target%%\?*}
target=${target%/}
contest=
only=
if [[ "$target" =~ /contests/([^/]+)/tasks/([^/]+)$ ]]; then
  contest=${BASH_REMATCH[1]}
  only=${BASH_REMATCH[2]}
elif [[ "$target" =~ /contests/([^/]+)(/tasks)?$ ]]; then
  contest=${BASH_REMATCH[1]}
elif [[ "$target" != *://* ]]; then
  contest=$target
else
  echo "unrecognized target: ${target}" >&2
  exit 2
fi

root=$(cd "$(dirname "$0")/.." && pwd)
if [[ -n "$only" ]]; then
  problems=("$only")
else
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
fi

echo "contest ${contest}: ${#problems[@]} problems -> ${folder}/"
shim=$(mktemp -d)
trap 'rm -rf "$shim"' EXIT
cat > "${shim}/pkg_resources.py" << 'PY'
import importlib.resources as resources

def resource_filename(package, resource):
    return str(resources.files(package).joinpath(resource))
PY
nix shell nixpkgs#online-judge-tools nixpkgs#online-judge-template-generator --command \
  env PYTHONPATH="$shim" bash -s -- "$root" "$contest" "$folder" "${problems[@]}" << 'EOF'
set -euo pipefail
root=$1
contest=$2
folder=$3
shift 3
for problem_id in "$@"; do
  if [[ "$folder" == src && -e "${root}/src/dp/${problem_id}/test/sample-1.in" ]]; then
    echo "skip ${problem_id} (src/dp/${problem_id}/test/sample-1.in already exists)"
    continue
  fi
  dir="${root}/${folder}/${problem_id}"
  mkdir -p "$dir"
  if [[ -e "${dir}/test/sample-1.in" ]]; then
    echo "skip ${problem_id} (${folder}/${problem_id}/test/sample-1.in already exists)"
  else
    echo "download ${problem_id} -> ${folder}/${problem_id}/test"
    (
      cd "$dir"
      oj download "https://atcoder.jp/contests/${contest}/tasks/${problem_id}"
    )
  fi
  if [[ ! -e "${dir}/main.py" ]]; then
    echo "template ${problem_id} -> ${folder}/${problem_id}/main.py"
    (
      cd "$dir"
      oj-template -t "${root}/scripts/template/main.py" "https://atcoder.jp/contests/${contest}/tasks/${problem_id}" > main.py
    )
  fi
done
EOF
