import csv
import os
import re

COLUMNS_TO_REMOVE = {"3PA_Share", "2PA_Share", "3PM_Share", "2PM_Share"}

def year_to_start_year(year_value: str) -> str:
    """
    Converts:
      '1990-91' -> '1990'
      '1990–91' -> '1990' (en dash)
      '1990'    -> '1990'
    """
    if year_value is None:
        return ""
    s = str(year_value).strip()
    if s == "":
        return ""

    # normalize dash types
    s = s.replace("–", "-").replace("—", "-")

    m = re.match(r"^(\d{4})-\d{2}$", s)
    if m:
        return m.group(1)
    return s

def find_year_column(fieldnames):
    """
    Try to find a year/season column in a flexible way.
    Prefers: Year, Season (case-insensitive)
    """
    if not fieldnames:
        return None

    lower_map = {c.lower(): c for c in fieldnames}

    # common names
    for key in ["year", "season"]:
        if key in lower_map:
            return lower_map[key]

    # fallback: anything containing year/season
    for c in fieldnames:
        cl = c.lower()
        if "year" in cl or "season" in cl:
            return c

    return None

def clean_file(input_path: str) -> str:
    folder = os.path.dirname(input_path)
    base = os.path.basename(input_path)
    name, ext = os.path.splitext(base)

    output_path = os.path.join(folder, f"{name}_cleaned{ext}")

    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"No header found in {input_path}")

        # Remove only the columns that actually exist in this file
        new_fieldnames = [c for c in reader.fieldnames if c not in COLUMNS_TO_REMOVE]

        # Detect year/season column name (could be Year or Season, etc.)
        year_col = find_year_column(new_fieldnames)

        rows_out = []
        for row in reader:
            # Keep only desired columns (drops share columns when present)
            new_row = {k: row.get(k, "") for k in new_fieldnames}

            # Convert Year/Season format if the column exists
            if year_col:
                new_row[year_col] = year_to_start_year(new_row.get(year_col))

            rows_out.append(new_row)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    return output_path

def main():
    files_to_clean = [
        r"PF_C_team_averages_all_years.csv",
        r"PF_C_yearly_summary.csv",
        r"nba_team_records_1990_2025.csv",
    ]

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for file_path in files_to_clean:
        if not os.path.isabs(file_path):
            file_path = os.path.join(script_dir, file_path)

        if not os.path.exists(file_path):
            print(f"Skipping (not found): {file_path}")
            continue

        out = clean_file(file_path)
        print(f"Cleaned -> {out}")

if __name__ == "__main__":
    main()