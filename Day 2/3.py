import shutil #shutil.move() moves files
from pathlib import Path # Creates file paths safely across Windows

def archive_csvs(source_dir: str,target_dir: str) -> int: # int -> function return an integer(number of files moved)
    source = Path(source_dir) 
    target = Path(target_dir)
    # convert text path to Path object

    target.mkdir(parents=True, exist_ok=True)
    # mkdir -> Create parents folder
    # exist_ok -> Don't crash if folder already exists

    csv_files = list(source.glob('*.csv'))
    # .glob -> Find all .csv files in source folder

    if not csv_files:
        print(f'[INFO] No CSVs found in '{source}'. Pipeline idle. Exiting cleanly.')
        return 0
    
    moved_count = 0
    for file in csv_files:
        shutil.move(str(file),str(target/file.name))
        moved_count += 1

    print(f"[SUCCESS] Archived {moved_count} files to '{target}'.")
    return moved_count

if __name__ == "__main__":
    archive_csvs('./raw_data', './archive')
    