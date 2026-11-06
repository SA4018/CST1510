
"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

# ==================================================================== INPUT
# Check records until the user types quit as the hostname.
over_limit_count = 0

while True:
    hostname = input("Hostname (or quit): ")

    if hostname == "quit":
        break

    gb_used = float(input("GB used: "))
    gb_total = float(input("GB total: "))

    # ================================================================== PROCESS
    gb_difference = gb_total - gb_used
    used_percentage = (gb_used / gb_total) * 100

    if used_percentage >= 100:
        status = "OVER LIMIT"
    elif used_percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        over_limit_count += 1

    # =================================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used (GB)   : {gb_used:>10.2f}")
    print(f"  Total (GB)  : {gb_total:>10.2f}")
    print(f"  Free (GB)   : {gb_difference:>+10.2f}")
    print(f"  Used (%)    : {used_percentage:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print(f"Total OVER LIMIT records: {over_limit_count}")
