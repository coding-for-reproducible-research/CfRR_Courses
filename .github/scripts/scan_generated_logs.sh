#!/usr/bin/env bash
set -euo pipefail

scan_root="${1:-_build}"
config_path="${2:-.gitleaks.toml}"

if [ ! -d "$scan_root" ]; then
  echo "Generated log directory not found: $scan_root"
  exit 0
fi

mapfile -d '' log_files < <(
  find "$scan_root" -type f \
    \( -name "*.log" -o -name "*.err" -o -name "*.out" \) \
    -print0
)

if [ "${#log_files[@]}" -eq 0 ]; then
  echo "No generated logs found to scan."
  exit 0
fi

config_args=()
if [ -f "$config_path" ]; then
  config_args+=(--config "$config_path")
fi

scan_exit=0
for log_file in "${log_files[@]}"; do
  echo "Scanning generated log: $log_file"
  set +e
  gitleaks dir "$log_file" \
    "${config_args[@]}" \
    --redact=100 \
    --no-banner \
    --log-level warn \
    --exit-code 1
  exit_code=$?
  set -e

  if [ "$exit_code" -ne 0 ]; then
    scan_exit="$exit_code"
  fi
done

exit "$scan_exit"
