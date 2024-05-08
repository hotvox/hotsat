#!/bin/bash
script_dir=$(cd "$(dirname "$0")" || exit; pwd)
project_dir=$(cd "$script_dir"/.. || exit; pwd)
export_path="$project_dir"/hotsat.zip

cd "$project_dir" || exit
zip -r "$export_path" . -x hotsat.zip -x __pycache__/\* -x \*/__pycache__/\* -x .git/\*