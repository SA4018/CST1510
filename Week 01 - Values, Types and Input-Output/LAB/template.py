
"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

# ==================================================================== INPUT
hostname = input("Hostname: ")
gb_used = float(input("GB used: "))
gb_total = float(input("GB total: "))

# ================================================================== PROCESS
# A positive difference means free storage; a negative value means over capacity.
gb_difference = gb_total - gb_used
used_percentage = (gb_used / gb_total) * 100

# The remaining percentage helps estimate available storage at a glance.
free_percentage = (gb_difference / gb_total) * 100

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used (GB)   : {gb_used:>10.2f}")
print(f"  Total (GB)  : {gb_total:>10.2f}")
print(f"  Free (GB)   : {gb_difference:>+10.2f}")
print(f"  Used (%)    : {used_percentage:>10.2f} %")
print(f"  Free (%)    : {free_percentage:>10.2f} %")
print("=" * 34)
