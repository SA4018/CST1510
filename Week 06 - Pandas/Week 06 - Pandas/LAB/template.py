"""
RECORD CHECK - my version
=========================

Name : Your Name
Lane : IT
Date : Your Date

Run it: python template.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
lab_folder = Path(__file__).resolve().parent
input_file = lab_folder / "records.csv"
report_file = lab_folder / "records_report.csv"
chart_file = lab_folder / "status_counts.png"

df = pd.read_csv(input_file)

# ================================================================= PROCESS
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

# ================================================================== OUTPUT
print("All records:")
print(df.to_string(index=False))

print("\nRecords needing attention:")
print(df[df["status"] != "OK"].to_string(index=False))

status_counts = df.groupby("status").size()

print("\nCounts by status:")
print(status_counts.to_string())

df.to_csv(report_file, index=False)

status_counts.plot(
    kind="bar",
    title="Record Status Counts",
    rot=0
)

plt.xlabel("Status")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig(chart_file)
plt.close()

print(f"\nSaved {report_file.name} and {chart_file.name}")
