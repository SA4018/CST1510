
"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

# ================================================================= FUNCTIONS
def status_of(percent):
    """Return OK, WARNING, or OVER LIMIT for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return free space and the percentage of capacity used."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
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


# ================================================== INPUT / PROCESS / OUTPUT
over_limit_count = 0

while True:
    label = input("Hostname (or quit): ")

    if label == "quit":
        break

    value = float(input("GB used: "))
    limit = float(input("GB total: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Total OVER LIMIT records: {over_limit_count}")
