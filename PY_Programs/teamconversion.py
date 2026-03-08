import csv
import os

# ====== CHANGE THIS IF NEEDED ======
input_file = "nba_team_records_1990_2025.csv"
output_file = "nba_team_records_1990_2025_cleaned.csv"
# ==================================

city_changes = {
    "Vancouver": "Memphis",
    "Seattle": "Oklahoma",
    "New Jersey": "Brooklyn",
}

name_changes = {
    "Bullets": "Wizards",
    "SuperSonics": "Thunder",
    "Bobcats": "Hornets",
}

# Full team name -> abbreviation (includes common historical/renamed cases)
team_to_abv = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "New Jersey Nets": "BKN",          # just in case a row still has this after merge logic
    "Charlotte Hornets": "CHA",
    "Charlotte Bobcats": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "LA Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "LA Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Vancouver Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New Orleans Hornets": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Oklahoma Thunder": "OKC",          # because you asked for Seattle -> Oklahoma
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",
    "Washington Bullets": "WAS",
}

def normalize(s: str) -> str:
    return (s or "").strip()

def main():
    # If user left input_file as just a filename, assume it's in the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    in_path = input_file if os.path.isabs(input_file) else os.path.join(script_dir, input_file)
    out_path = output_file if os.path.isabs(output_file) else os.path.join(script_dir, output_file)

    with open(in_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("No header row found in the CSV.")
        fieldnames = list(reader.fieldnames)

        # Ensure required columns exist
        required = ["TeamCity", "TeamName"]
        for col in required:
            if col not in fieldnames:
                raise ValueError(f"Missing required column: {col}")

        # Add new columns if they don't exist
        if "Team" not in fieldnames:
            fieldnames.append("Team")
        if "TeamAbv" not in fieldnames:
            fieldnames.append("TeamAbv")

        rows_out = []

        for row in reader:
            city = normalize(row.get("TeamCity"))
            name = normalize(row.get("TeamName"))

            # Apply direct replacements
            city = city_changes.get(city, city)
            name = name_changes.get(name, name)

            # Apply IF rules based on (updated) city
            if city == "Charlotte":
                name = "Hornets"
            if city == "New Orleans":
                name = "Pelicans"

            team_full = f"{city} {name}".strip()

            # Add abbreviation
            abv = team_to_abv.get(team_full, "")

            # Write back to row
            row["TeamCity"] = city
            row["TeamName"] = name
            row["Team"] = team_full
            row["TeamAbv"] = abv

            rows_out.append(row)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    print(f"Done! Wrote cleaned file to:\n{out_path}")

if __name__ == "__main__":
    main()