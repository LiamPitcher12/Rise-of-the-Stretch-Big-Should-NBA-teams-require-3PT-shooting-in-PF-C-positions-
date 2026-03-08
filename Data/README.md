# Data-Sets Description and Summary

This project uses several datasets constructed from historical NBA statistics covering approximately 30 years of league data. The datasets include player-level shooting statistics for power forwards and centers, processed team-level shooting data for frontcourt players, and overall team performance records. Raw player statistics were collected and organized by season, then cleaned and aggregated using Python scripts to produce consistent datasets suitable for analysis. Together, these datasets allow the project to examine long-term trends in frontcourt shooting behavior and explore how changes in power forward and center shot selection relate to team performance and roster construction strategies.

## Dataset 1: Raw Data (1990-2024)

The raw data folder contains the original season-level player statistics downloaded from Basketball-Reference for each NBA season between 1990 and 2024. Each file includes individual player shooting statistics for a given season, including metrics such as field goals, three-point attempts, two-point attempts, and other shooting indicators. These files represent the unprocessed source data used to construct the project datasets. The raw player data was later filtered and cleaned using Python scripts to isolate frontcourt positions and standardize the data across seasons before aggregation and analysis.

## Dataset 2: PF_C Data (1990-2024)

The PF_C dataset contains processed player shooting data specifically for power forwards and centers for each NBA season from 1990 to 2024. These files were created by filtering the raw player statistics to include only frontcourt positions and standardizing team abbreviations, season formats, and statistical columns. Each file represents one NBA season and provides shooting statistics for power forwards and centers, including metrics such as three-point attempts, two-point attempts, shooting percentages, and other offensive indicators. This dataset allows the project to analyze how shot selection for frontcourt players has changed over time and whether perimeter shooting has become more common among big men.

## Dataset 3: Summary Data

The summary datasets were created by aggregating the cleaned PF_C data to produce higher-level statistics used for analysis.

### (3.1) "PF_C_team_averages_all_years_cleaned.csv"

This dataset contains team-level averages for power forwards and centers across all NBA teams from 1990 to 2024. The data aggregates frontcourt player statistics by team and season, providing average shooting metrics such as three-point attempts, two-point attempts, and shooting percentages. This dataset allows the project to examine how teams utilize frontcourt players offensively and whether perimeter shooting by big men has increased across the league.

### (3.2) "PF_C_yearly_summary_cleaned.csv"

This dataset contains league-wide yearly averages of shooting statistics for power forwards and centers from 1990 to 2024. The data summarizes frontcourt shooting behavior for each season and highlights long-term trends in shot selection, particularly the shift between two-point and three-point attempts.

### (3.3) "nba_team_records_1990_2025_cleaned.csv"

This dataset contains team performance records for NBA teams between 1990 and 2025, including wins, losses, and overall team success metrics. The dataset is used to compare team performance with frontcourt shooting trends, allowing the project to explore whether teams that incorporate perimeter shooting from power forwards and centers tend to achieve greater competitive success.