import os
import re
import csv
from collections import defaultdict

# --- Abbreviation fixes (if any old ones show up) ---
abv_fixes = {
    "WSB": "WSH",
    "VAN": "MEM",
    "SEA": "OKC",
    "NJN": "BKN",
    "CHB": "CHA",
    "CHH": "CHA",
    "NOH": "NOP",
}

# --- Team abbreviation -> full team name (covers modern + key historical abbrevs) ---
abv_to_name = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "BKN": "Brooklyn Nets",
    "CHA": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOP": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHX": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "TOR": "Toronto Raptors",
    "UTA": "Utah Jazz",
    "WAS": "Washington Wizards",
}

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

def is_real_team_abv(team: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{3}", team or ""))

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

            non_numeric = {"Player", "Age", "Team", "Pos"}
            stat_cols = [c for c in reader.fieldnames if c not in non_numeric]

            # These are the columns we want TOTALS for (only if they exist in the file)
            total_candidate_cols = ["3P", "3PA", "2P", "2PA", "FG", "FGA", "FT", "FTA"]
            total_cols = [c for c in total_candidate_cols if c in stat_cols]

            # Sums and counts for averages
            sums = defaultdict(lambda: defaultdict(float))
            counts = defaultdict(lambda: defaultdict(int))

            # Separate sums for totals (counts)
            totals = defaultdict(lambda: defaultdict(float))

            for row in reader:
                team = (row.get("Team") or "").strip()
                team = abv_fixes.get(team, team)

                if not is_real_team_abv(team):
                    continue

                # averages for all stat columns
                for col in stat_cols:
                    val = safe_float(row.get(col))
                    if val is None:
                        continue
                    sums[team][col] += val
                    counts[team][col] += 1

                # totals for shot count columns
                for col in total_cols:
                    val = safe_float(row.get(col))
                    if val is None:
                        continue
                    totals[team][col] += val

            # Build output rows (team averages + totals for this year)
            for team in sorted(sums.keys()):
                out = {
                    "Year": year,
                    "TeamAbv": team,
                    "TeamName": abv_to_name.get(team, ""),
                }

                # averages (3 decimals)
                for col in stat_cols:
                    if counts[team][col] > 0:
                        avg = sums[team][col] / counts[team][col]
                        out[col] = f"{avg:.3f}"
                    else:
                        out[col] = ""

                # totals (keep as whole-ish numbers; still safe to format)
                for col in total_cols:
                    out[f"TOTAL_{col}"] = f"{totals[team][col]:.3f}" if totals[team][col] else "0.000"

                # header
                if output_header is None:
                    output_header = ["Year", "TeamAbv", "TeamName"] + stat_cols + [f"TOTAL_{c}" for c in total_cols]

                output_rows.append(out)

    out_path = os.path.join(folder, "PF_C_team_averages_all_years.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=output_header)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Done! Created: {out_path}")

if __name__ == "__main__":
    main()