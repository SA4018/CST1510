
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
def check_record(value, limit):
    """Return free capacity, usage percentage, and status for one record."""
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Display a formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used (GB)   : {value:>10.2f}")
    print(f"  Total (GB)  : {limit:>10.2f}")
    print(f"  Free (GB)   : {difference:>+10.2f}")
    print(f"  Used (%)    : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


def load_records(path):
    """Load comma-separated label, value, and limit records from a file."""
    records = []

    with open(path, encoding="utf-8") as source:
        for line in source:
            if not line.strip():
                continue

            label, value, limit = line.strip().split(",")

            records.append({
                "label": label.strip(),
                "value": float(value),
                "limit": float(limit),
            })

    return records


def save_results(path, results):
    """Write one label and status per line to a results file."""
    with open(path, "w", encoding="utf-8") as destination:
        for label, status in results:
            destination.write(f"{label},{status}\n")


# =============================================================== STORE / INPUT
lab_folder = Path(__file__).resolve().parent
input_file = lab_folder / "records.txt"
output_file = lab_folder / "results.txt"

try:
    records = load_records(input_file)
except FileNotFoundError:
    print(f"Input file not found: {input_file.name}")
    records = []


# ============================================================ PROCESS / OUTPUT
over_limit_count = 0
results = []

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"], record["value"], record["limit"],
        difference, percent, status
    )

    results.append((record["label"], status))

    if status == "OVER LIMIT":
        over_limit_count += 1

save_results(output_file, results)

print(f"Checked {len(records)} records. {over_limit_count} were OVER LIMIT.")
