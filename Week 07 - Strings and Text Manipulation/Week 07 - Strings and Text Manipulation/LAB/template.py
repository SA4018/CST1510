"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

from pathlib import Path

# ================================================================= FUNCTIONS
def parse_line(raw_line):
    """Convert a messy IT record into a clean dictionary."""
    parts = raw_line.strip().lower().split(",")

    if len(parts) != 3:
        raise ValueError("Expected a hostname and two numeric fields")

    record = {"hostname": parts[0].strip()}

    for field in parts[1:]:
        key, value = field.split("=", 1)
        record[key.strip()] = float(value.strip())

    return record


def status_of(used, total):
    """Classify storage usage as OK, WARNING, or OVER LIMIT."""
    percent = (used / total) * 100

    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


# ===================================================================== INPUT
lab_folder = Path(__file__).resolve().parent
input_file = lab_folder / "messy_records.txt"

with open(input_file, encoding="utf-8") as source:
    raw_records = [line for line in source if line.strip()]


# =========================================================== PROCESS + OUTPUT
flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])

    print(f"{record} -> {status}")

    if status != "OK":
        flagged += 1

print(f"Checked {len(raw_records)} records. {flagged} were flagged.")
