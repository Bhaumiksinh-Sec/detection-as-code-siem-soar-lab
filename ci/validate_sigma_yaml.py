import sys
from pathlib import Path

import yaml

REQUIRED_TOP_LEVEL_KEYS = {
    "title",
    "id",
    "status",
    "description",
    "logsource",
    "detection",
}

def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{path}: YAML parse error: {e}"]

    if not isinstance(data, dict):
        return [f"{path}: Expected YAML document to be a mapping/object"]

    missing = REQUIRED_TOP_LEVEL_KEYS - set(data.keys())
    if missing:
        errors.append(f"{path}: Missing required keys: {', '.join(sorted(missing))}")

    # Basic detection sanity
    det = data.get("detection")
    if det is not None and not isinstance(det, dict):
        errors.append(f"{path}: 'detection' must be a mapping/object")

    # Basic logsource sanity
    ls = data.get("logsource")
    if ls is not None and not isinstance(ls, dict):
        errors.append(f"{path}: 'logsource' must be a mapping/object")

    return errors

def main() -> int:
    base = Path("detections")
    if not base.exists():
        print("No detections/ directory found. Nothing to validate.")
        return 0

    yml_files = sorted(list(base.rglob("*.yml")) + list(base.rglob("*.yaml")))
    if not yml_files:
        print("No detection YAML files found under detections/. Nothing to validate.")
        return 0

    all_errors: list[str] = []
    for f in yml_files:
        all_errors.extend(validate_file(f))

    if all_errors:
        print("❌ Validation failed:\n")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"✅ Validation passed for {len(yml_files)} detection file(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
