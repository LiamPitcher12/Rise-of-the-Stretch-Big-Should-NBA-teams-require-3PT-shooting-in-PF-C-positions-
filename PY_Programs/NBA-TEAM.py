from nba_api.stats.endpoints import leaguestandings
import pandas as pd
import time

# Convert year → NBA season format (1990 → 1990-91)
def format_season(year):
    return f"{year}-{str(year+1)[-2:]}"

all_data =[]

for year in range(1990, 2025):
    season = format_season(year)
    print(f"Fetching {season}...")

    try:
        standings = leaguestandings.LeagueStandings(
        season=season
        ).get_data_frames()[0]

        standings["SEASON"] = season

        # Select stable column names (based on your output)
        cleaned = standings[
        [
        "SEASON",
        "TeamID",
        "TeamCity",
        "TeamName",
        "Conference",
        "WINS",
        "LOSSES",
        "WinPCT",
        ]
        ].copy()

        # Standardize column names
        cleaned.rename(
        columns={
        "WINS": "W",
        "LOSSES": "L",
        "WinPCT": "W_PCT",
        },
        inplace=True,
        )

        all_data.append(cleaned)

    except Exception as e:
        print(f"Error fetching {season}: {e}")

    # Avoid API rate limits
    time.sleep(1.5)

# Combine all seasons
final_df = pd.concat(all_data, ignore_index=True)

# Save to CSV
final_df.to_csv("nba_team_records_1990_2025.csv", index=False)

print("Done. File saved as nba_team_records_1990_2025.csv")