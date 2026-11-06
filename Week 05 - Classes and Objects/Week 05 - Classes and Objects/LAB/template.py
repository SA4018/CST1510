
"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

from pathlib import Path


# ====================================================================== CLASS
class Record:
    """Represent one storage record."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the label, used space, and total space."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the storage usage status."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Load comma-separated records as Record objects."""
    records = []

    with open(path, encoding="utf-8") as source:
        for line in source:
            if not line.strip():
                continue

            label, value, limit = line.strip().split(",")

            records.append(
                Record(label.strip(), float(value), float(limit))
            )

    return records


lab_folder = Path(__file__).resolve().parent
records = load_records(lab_folder / "records.txt")


# ===================================================================== OUTPUT
Record.over_limit_count = 0

for record in records:
    status = record.status()

    if status == "OVER LIMIT":
        Record.over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used (GB)   : {record.value:>10.2f}")
    print(f"  Total (GB)  : {record.limit:>10.2f}")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print(f"Total OVER LIMIT records: {Record.over_limit_count}")
