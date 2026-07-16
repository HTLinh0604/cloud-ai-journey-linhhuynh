import os
import glob
import re

base_dir = r"d:\22DKHA1\AWS\FCAJ-workshop\content\1-Worklog"
weeks = sorted(os.listdir(base_dir), key=lambda x: [float(i) if '.' in x else x for i in re.findall(r'\d+\.\d+|\d+', x)] or [x])

print("Weeks found:", weeks)

for week in weeks:
    path = os.path.join(base_dir, week, "_index.md")
    if os.path.exists(path):
        print(f"\n=================== {week} ===================")
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print("".join(lines[:25])) # Print first 25 lines
            print("...")
            print("".join(lines[-25:])) # Print last 25 lines
