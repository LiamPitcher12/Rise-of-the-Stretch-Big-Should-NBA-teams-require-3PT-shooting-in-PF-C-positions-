import csv
import re

INPUT_FILE = "Player90-91-Raw.csv"
OUTPUT_FILE = "PF_C_shooting90-91.csv"

MULTI_TEAM_PATTERN = re.compile(r"^\s*\d+\s*TM\s*$", re.IGNORECASE)

def pos_is_pf_or_c(pos_value: str) -> bool:
    if not pos_value:
        return False
    tokens = re.split(r"[^A-Z]+", pos_value.upper())
    tokens = [t for t in tokens if t]
    return ("PF" in tokens) or ("C" in tokens)

def team_is_multiteam(team_value: str) -> bool:
    if not team_value:
        return False
    return bool(MULTI_TEAM_PATTERN.match(team_value.strip()))

def to_int(x):
    try:
        return int(x)
    except:
        return None

def safe_div(n, d):
    return (n / d) if d else None

def fmt3(x):
    return "" if x is None else f"{x:.3f}"

def main():
    # Dedup: Player -> (is_multiteam:int, row_index:int, row_dict)
    best_by_player = {}
    header = None

    with open(INPUT_FILE, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        if not header:
            raise ValueError("No header row found in the CSV.")

        # minimal required columns
        required = ["Player", "Age", "Team", "Pos", "3P", "3PA", "3P%", "2P", "2PA", "2P%"]
        missing = [c for c in required if c not in header]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        for idx, row in enumerate(reader):
            player = (row.get("Player") or "").strip()
            team = (row.get("Team") or "").strip()
            pos = (row.get("Pos") or "").strip()

            if not player or not pos_is_pf_or_c(pos):
                continue

            is_multi = 1 if team_is_multiteam(team) else 0

            if player not in best_by_player:
                best_by_player[player] = (is_multi, idx, row)
            else:
                prev_multi, prev_idx, _ = best_by_player[player]
                if is_multi > prev_multi or (is_multi == prev_multi and idx < prev_idx):
                    best_by_player[player] = (is_multi, idx, row)

    # Sort output rows back to file order
    kept = sorted(best_by_player.values(), key=lambda t: t[1])

    # Totals for summary (makes/attempts)
    total_3p = 0
    total_3pa = 0
    total_2p = 0
    total_2pa = 0

    out_cols = ["Player", "Age", "Team", "Pos", "3P", "3PA", "3P%", "2P", "2PA", "2P%"]
    # extra summary-only columns
    extra_cols = ["3PA_Share", "2PA_Share", "3PM_Share", "2PM_Share"]
    out_fieldnames = out_cols + extra_cols

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fieldnames)
        writer.writeheader()

        for _is_multi, _idx, row in kept:
            # write player row
            out_row = {c: row.get(c, "") for c in out_cols}
            out_row.update({c: "" for c in extra_cols})
            writer.writerow(out_row)

            # accumulate totals (skip blanks/non-ints safely)
            v3p = to_int(row.get("3P", ""))
            v3pa = to_int(row.get("3PA", ""))
            v2p = to_int(row.get("2P", ""))
            v2pa = to_int(row.get("2PA", ""))

            if v3p is not None: total_3p += v3p
            if v3pa is not None: total_3pa += v3pa
            if v2p is not None: total_2p += v2p
            if v2pa is not None: total_2pa += v2pa

        # SUMMARY metrics
        weighted_3p_pct = safe_div(total_3p, total_3pa)          # makes / attempts
        weighted_2p_pct = safe_div(total_2p, total_2pa)

        total_shots = total_3pa + total_2pa
        share_3pa = safe_div(total_3pa, total_shots)
        share_2pa = safe_div(total_2pa, total_shots)

        total_makes = total_3p + total_2p
        share_3pm = safe_div(total_3p, total_makes)
        share_2pm = safe_div(total_2p, total_makes)

        
    print(f"Saved {len(kept)} PF/C rows + summary to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()