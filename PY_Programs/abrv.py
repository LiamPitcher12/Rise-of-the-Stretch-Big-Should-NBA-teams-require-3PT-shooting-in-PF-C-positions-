import os
import csv

# Folder where the script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

team_changes = {
    "WSB": "WAS",
    "VAN": "MEM",
    "SEA": "OKC",
    "NJN": "BKN",
    "CHB": "CHA",
    "CHH": "CHA",
    "NOH": "NOP",
    "BRK": "BKN",
    "CHO": "CHA",
    "PHO": "PHX",
    "NOK": "NOP",
    "WSH": "WAS"
}

for filename in os.listdir(folder_path):
    if filename.startswith("PF_C_shooting") and filename.endswith(".csv"):

        file_path = os.path.join(folder_path, filename)

        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

        if not rows:
            continue

        header = rows[0]

        # Find team column
        if "Team" in header:
            team_index = header.index("Team")
        elif "Tm" in header:
            team_index = header.index("Tm")
        else:
            print(f"No team column found in {filename}")
            continue

        # Update rows
        for row in rows[1:]:
            if len(row) > team_index and row[team_index] in team_changes:
                row[team_index] = team_changes[row[team_index]]

        # Write updated file
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print(f"Updated: {filename}")