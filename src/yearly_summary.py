import os
import re
import csv

def parse_year_from_filename(filename: str) -> str:
    """
    PF_C_shooting96-97.csv -> 1996-97
    PF_C_shooting03-04.csv -> 2003-04
    """
    m = re.search(r"PF_C_shooting(\d{2}-\d{2})", filename)
    if not m:
        return ""
    yy1, yy2 = m.group(1).split("-")
    start_year = 1900 + int(yy1) if int(yy1) >= 70 else 2000 + int(yy1)
    return f"{start_year}-{yy2}"

def safe_float(x):
    try:
        if x is None:
            return None
        x = str(x).strip()
        if x == "":
            return None
        return float(x)
    except:
        return None

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    files = sorted(
        f for f in os.listdir(folder)
        if f.startswith("PF_C_shooting") and f.endswith(".csv")
    )

    if not files:
        print("No files found starting with 'PF_C_shooting' in this folder.")
        return

    output_rows = []
    output_header = None

    for fn in files:
        year = parse_year_from_filename(fn)
        path = os.path.join(folder, fn)

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print(f"Skipping (no header found): {fn}")
                continue

            # Stat columns = everything except obvious non-numeric fields
            non_numeric = {"Player", "Age", "Team", "Pos"}
            stat_cols = [c for c in reader.fieldnames if c not in non_numeric]

            # Columns to total (only if present)
            total_candidate_cols = ["3P", "3PA", "2P", "2PA", "FG", "FGA", "FT", "FTA"]
            total_cols = [c for c in total_candidate_cols if c in stat_cols]

            sums = {c: 0.0 for c in stat_cols}
            counts = {c: 0 for c in stat_cols}

            totals = {c: 0.0 for c in total_cols}

            for row in reader:
                # averages
                for col in stat_cols:
                    val = safe_float(row.get(col))
                    if val is None:
                        continue
                    sums[col] += val
                    counts[col] += 1

                # totals
                for col in total_cols:
                    val = safe_float(row.get(col))
                    if val is None:
                        continue
                    totals[col] += val

            out = {"Year": year}

            # Averages (3 decimals)
            for col in stat_cols:
                if counts[col] > 0:
                    avg = sums[col] / counts[col]
                    out[col] = f"{avg:.3f}"
                else:
                    out[col] = ""

            # Totals (3 decimals for consistent formatting)
            for col in total_cols:
                out[f"TOTAL_{col}"] = f"{totals[col]:.3f}"

            # Header: Year + stat cols + total cols
            if output_header is None:
                output_header = ["Year"] + stat_cols + [f"TOTAL_{c}" for c in total_cols]

            output_rows.append(out)

    out_path = os.path.join(folder, "PF_C_yearly_summary.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=output_header)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Done! Created: {out_path}")

if __name__ == "__main__":
    main()