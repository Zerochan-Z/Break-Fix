import os
import shutil

os.mkdir("archive")  # Break 1: Crashes if folder already exists

files = os.listdir("raw_data")

for f in files:
    if f.endswith(".csv"):
        shutil.move(f"raw_data/{f}", f"archive/{f}")

print("Done!")  # Break 2: Prints "Done!" even if 0 files moved