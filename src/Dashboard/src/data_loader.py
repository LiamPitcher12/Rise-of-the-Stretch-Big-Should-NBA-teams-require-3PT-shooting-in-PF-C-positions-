from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

def _read_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW / name)

def _load_player_files() -> pd.DataFrame:
    frames = []
    for path in sorted(RAW.glob("PF_C_shooting*.csv")):
        df = pd.read_csv(path)
        stem = path.stem.replace("PF_C_shooting", "")
        start = int(stem[:2])
        year = 1900 + start if start >= 90 else 2000 + start
        df["Year"] = year
        frames.append(df)
    players = pd.concat(frames, ignore_index=True)
    return players

def load_data():
    yearly = _read_csv("PF_C_yearly_summary_cleaned.csv")
    team = _read_csv("PF_C_team_averages_all_years_cleaned.csv")
    records = _read_csv("nba_team_records_1990_2025_cleaned.csv").rename(columns={"YEAR": "Year"})
    merged = team.merge(records[["Year", "TeamAbv", "Conference", "W", "L", "W_PCT"]], on=["Year", "TeamAbv"], how="left")
    players = _load_player_files()
    return {"yearly": yearly, "team": merged, "players": players}