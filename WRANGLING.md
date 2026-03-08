# Data Wrangling
## Overview:

The goal of the wrangling process was to transform raw NBA player and team statistics into a clean, consistent, and analysis-ready set of datasets focused on the evolution of power forwards and centers over approximately 30 years. The final project required more than simply downloading historical statistics. The raw data had to be cleaned, filtered, standardized, and aggregated across dozens of season files before it could be used to answer the project’s decision question: whether three-point shooting should be treated as a required skill in modern big-man development and roster construction.

The wrangling process was completed primarily in Python using Visual Studio Code. Python scripts were used to automate repetitive cleaning tasks across many CSV files, including filtering positions, standardizing historical team information, removing unnecessary variables, converting season labels into a consistent format, and generating summary datasets. ChatGPT (OpenAI) was also used as an AI-assisted programming support tool to help build, troubleshoot, and refine several of the Python scripts used in the cleaning and aggregation process.

## The workflow moved through three major stages:

Raw Data – original season-level player files

PF_C Data – cleaned season-level files containing only power forwards and centers

Summary Data – aggregated datasets used for trend analysis and comparison with team success

## Tools Used

### The data wrangling process used the following tools:

- Python – used to automate filtering, cleaning, renaming, aggregation, and file creation

- Visual Studio Code – used to write, run, and debug Python scripts

- Python standard libraries (csv, os, re, collections)

- Microsoft Excel / CSV preview tools – used for spot-checking outputs and verifying cleaned files

- ChatGPT (OpenAI) – used as an AI-assisted programming aid to help develop and refine Python scripts for cleaning, transformation, troubleshooting, and aggregation

## Data Pipeline
### Stage 1: Raw Data

The raw data consisted of season-level NBA player statistics downloaded as CSV files for each season from 1990–91 through 2024–25. Each file contained player totals and included all positions, all teams, and all player records for that season.

These files served as the original source material for the project, but they were not immediately usable because they contained:

- players from all positions rather than only frontcourt players

- inconsistent team abbreviations across decades

- franchise relocations and name changes

- players who appeared under special trade tags such as 2TM

- season values formatted in a way that would complicate merging and time-series work

- columns not needed for this analysis

Because the research question focuses specifically on power forwards and centers, the raw files had to be transformed substantially before meaningful analysis could begin.

## Stage 2: PF_C Data

The second stage involved creating a separate set of files that included only power forwards and centers. This was done by filtering the raw player data by position and saving new season-level files for frontcourt players only.

These PF_C files still needed additional cleaning because even after filtering by position, the data still contained historical inconsistencies in franchise naming, season formatting, and redundant columns. This stage therefore acted as the bridge between the raw player-level data and the final summary datasets.

## Stage 3: Summary Data

The final stage involved aggregating the cleaned PF_C files into summary datasets that could be used directly for analysis and visualization.

### Three main summary datasets were created:

- PF_C_team_averages_all_years_cleaned.csv

- PF_C_yearly_summary_cleaned.csv

- nba_team_records_1990_2025_cleaned.csv

### These files were designed to answer different parts of the project:

- how PF/C shooting changed over time at the league level

- how PF/C shooting was used at the team level

- whether frontcourt shooting trends could be compared with team success

- Issues Encountered in the Raw Data

A major part of the wrangling process involved identifying and resolving inconsistencies in the original raw data.

## 1. Data spread across many separate files

The project covered roughly 30 years of NBA data, but the original statistics were stored in separate CSV files by season. This meant the same cleaning operations had to be repeated across many files.

To solve this, Python scripts were written to:

search through folders automatically

identify files based on naming patterns such as PF_C_shooting

apply the same transformations across all matching files

output standardized cleaned files

This reduced manual work and made the wrangling process reproducible.

## 2. Mixed positions in the raw player files

The raw player files contained all NBA players, including guards, wings, forwards, and centers. Since the project focuses on frontcourt role evolution, the dataset had to be narrowed to players whose position was relevant to the research question.

### The raw files were filtered to include only:

- PF

- C

This created the PF_C dataset family, which isolates the players most relevant to the question of whether big men have shifted toward perimeter shooting.

### 3. Midseason trades and multi-team rows (2TM, 3TM)

One of the most important data consistency issues involved players who were traded during the season. In Basketball-Reference style datasets, these players often appear more than once:

- once for each individual team they played for

- once again as a combined season total under a tag such as 2TM or 3TM

- This creates a serious duplication problem if not handled carefully.

#### Why this was an issue?

If a traded player’s team rows and combined 2TM row are all included in an aggregation, that player’s statistics are counted more than once. This would artificially inflate totals and distort averages.

#### For example:

- a player could appear once for Team A

- once for Team B

- once again as 2TM

If all three rows were included, his season would effectively be counted multiple times.

### How this was handled

The wrangling scripts were designed to recognize that values such as 2TM and 3TM are not real team abbreviations. When team-level aggregation was performed, only rows with valid three-letter NBA franchise abbreviations were kept, while multi-team combined tags were excluded.

This was especially important in the creation of:

team-level PF/C averages

team-level PF/C totals

team-level comparisons with win-loss records

Without this step, traded players would have caused duplicate counting and invalid team summaries.

4. Historical franchise changes and abbreviation inconsistencies

A major challenge in working with 30 years of NBA data is that teams do not remain static over time. Across the period covered in this project, several franchises changed:

city

team name

abbreviation

This meant the same franchise could appear under different labels depending on the season.

Examples of issues encountered
Abbreviation changes

WSB → WSH

VAN → MEM

SEA → OKC

NJN → BKN

CHH / CHB → CHA

NOH → NOP

City changes

Vancouver → Memphis

Seattle → Oklahoma City

New Jersey → Brooklyn

Team name changes

Bullets → Wizards

SuperSonics → Thunder

Bobcats → Hornets

Hornets (New Orleans context) → Pelicans

Why this mattered

If these differences were left unresolved, several problems would occur:

the same franchise would be treated as different teams in different years

team-level trends would be split across historical labels

summary datasets would not merge cleanly with team success data

visualizations would incorrectly show separate entities rather than one continuous franchise

How this was handled

Several scripts were written to standardize franchise identifiers across all datasets.

For abbreviation fields, historical codes were replaced with consistent modern abbreviations. For example:

WSB -> WSH
VAN -> MEM
SEA -> OKC
NJN -> BKN
CHH -> CHA
CHB -> CHA
NOH -> NOP

For the team records dataset, additional transformations were made using TeamCity and TeamName:

Vancouver was changed to Memphis

Seattle was changed to Oklahoma

New Jersey was changed to Brooklyn

and:

Bullets was changed to Wizards

SuperSonics was changed to Thunder

Bobcats was changed to Hornets

Additional logic was also added:

if TeamCity = Charlotte, then TeamName = Hornets

if TeamCity = New Orleans, then TeamName = Pelicans

These values were then merged into a single team field and matched to a standardized team abbreviation field (TeamAbv).

This was one of the most important steps in the entire wrangling process because it ensured that the same franchise could be tracked consistently across the full time period.

5. Inconsistent season formatting

Another issue involved how seasons were labeled. In the original files, seasons were often represented in the format:

1990-91
1996-97
2003-04

While this is readable, it becomes awkward when merging datasets, creating time-series visualizations, or sorting seasons numerically. To simplify analysis, season labels were converted to a single-year format using the starting year of the season.

Examples:

1990-91 → 1990

1992-93 → 1992

2003-04 → 2003

This made it easier to:

sort seasons chronologically

align team records with PF/C summaries

use the year as a continuous variable in graphs and later analysis

Scripts were updated to detect the year or season column flexibly, since not every file used the exact same column name.

6. Unnecessary and redundant variables

Some generated datasets contained share-based columns such as:

3PA_Share

2PA_Share

3PM_Share

2PM_Share

These were removed in later cleaning because they were not essential to the main research question and could be recreated if needed from the totals. Keeping too many derived columns would make the dataset harder to interpret and increase clutter in later visualizations.

Removing these variables made the final summary datasets cleaner and more focused on the measures central to the project:

three-point attempts

two-point attempts

shooting percentages

team totals

team averages

win-loss outcomes

7. Header and file-structure issues

Some scripts initially ran into issues because CSV files were not always interpreted the same way. In one case, a DictReader could not properly detect header fields, which caused an error when writing output files.

To fix this, the code was adjusted to read rows more defensively and detect key columns such as Team, Tm, Year, or Season more flexibly. This helped make the scripts robust enough to handle slight structural inconsistencies between files.

Cleaning and Transformation Process
Step 1: Filtering raw data into PF_C files

The first transformation step was to isolate frontcourt players from the raw season files. The raw player files included every player in the league, but the research question is specifically about power forwards and centers.

Each season file was filtered so that only players with relevant position designations were retained. These filtered outputs became the PF_C season files.

This step ensured that all later analysis was focused only on the frontcourt positions relevant to the decision-maker’s question.

Step 2: Standardizing team abbreviations in PF_C files

Once the PF_C files were created, they were still not fully consistent because historical franchise codes varied by era. Scripts were written to search all files beginning with PF_C_shooting and replace outdated abbreviations with standardized ones.

This allowed all team-level comparisons to use one common identifier system rather than mixing historical and modern codes.

Step 3: Creating team-level averages and totals

After the PF_C files were standardized, another script was built to scan all PF_C season files and generate one combined dataset containing team-level averages for PF/C shooting stats.

This script:

searched for all files beginning with PF_C_shooting

extracted the season from the filename

grouped rows by team

calculated average values for each stat for PF/C players on that team

added the full team name based on the abbreviation

formatted averages to three decimal places

Later, this script was expanded to also include team totals for shot-count variables such as:

3P

3PA

2P

2PA

FG

FGA

FT

FTA

This was important because averages alone do not fully show how much frontcourt players were actually contributing to a team’s shot profile. Totals provided additional context.

The result was the dataset:

PF_C_team_averages_all_years_cleaned.csv

This file shows, for each team and year, how power forwards and centers performed as shooters and how large their shot volumes were.

Step 4: Creating the yearly league summary

A separate script was then created to aggregate all PF_C files into a single yearly summary. Rather than grouping by team, this script grouped by season and produced one row per year.

This created:

league-wide averages for frontcourt shooting metrics

yearly totals for major shot-count variables

This file was especially useful for answering the first part of the research question:

Has the role of NBA power forwards and centers shifted toward perimeter shooting over the past 30 years?

Because it compresses the league’s frontcourt shooting profile into one row per season, it becomes very easy to visualize long-term trends in:

PF/C three-point attempts

PF/C two-point attempts

PF/C shooting percentages

shot volume changes over time

The result was the dataset:

PF_C_yearly_summary_cleaned.csv

Step 5: Cleaning the team records dataset

The team records dataset required a separate wrangling process because it used team city and team name fields rather than a single clean abbreviation. This dataset was intended to provide a measure of team success that could later be compared with frontcourt shooting patterns.

To prepare it, scripts were written to:

rename outdated cities

rename outdated team names

merge city and team name into one team label

generate a matching abbreviation field

standardize season values into a single start year

This produced:

nba_team_records_1990_2025_cleaned.csv

This step was necessary so the team success data could be matched more easily with the PF/C team-level shooting summaries.

From Raw Data to Final Analytical Datasets

The overall transformation can be summarized as follows.

Raw Data

Original season-level NBA player totals for all players and all teams.

PF_C Data

Filtered seasonal files containing only power forwards and centers, with standardized team abbreviations and cleaner structure.

Summary Data

Three aggregated datasets used directly for analysis:

PF_C_team_averages_all_years_cleaned.csv

Shows team-by-team, year-by-year PF/C averages and totals. Useful for comparing team frontcourt usage and linking frontcourt style to team performance.

PF_C_yearly_summary_cleaned.csv

Shows league-wide yearly PF/C shooting trends. Useful for analyzing long-term changes in the role of big men.

nba_team_records_1990_2025_cleaned.csv

Shows yearly team performance outcomes such as wins and losses. Useful for testing whether frontcourt shooting patterns are associated with team success.

Assumptions and Decisions Made During Cleaning

Several assumptions were required during the wrangling process.

1. Modern franchise identity was used for consistency

When a franchise changed city, name, or abbreviation, the data was standardized to a single consistent identity so that long-term trends would not be artificially split.

2. Multi-team trade rows were excluded from team-level aggregation

Rows such as 2TM and 3TM were treated as non-team summary rows and excluded where necessary to prevent duplicate counting.

3. Missing values were left blank rather than imputed

For shooting stats, blank or missing values were not artificially filled in. This avoided introducing assumptions that were not supported by the data.

4. Season was represented by starting year

The season 1990-91 was represented as 1990 to simplify joining, sorting, and graphing.

5. Derived share columns were removed

Columns such as 3PA_Share and 2PA_Share were removed because they were not central to the analysis and could be recalculated later if needed.

Why the Wrangling Process Matters

The wrangling process was not just a technical step. It directly shaped the quality and credibility of the analysis. Without cleaning the franchise changes, removing trade-related duplicate rows, filtering by position, and standardizing the season format, it would not be possible to make valid comparisons across 30 years of NBA data.

Because the research question depends on long-term consistency, this preparation work was essential. The final datasets now provide a reliable foundation for examining whether power forwards and centers have shifted toward perimeter shooting and whether teams should treat three-point shooting as a required skill in big-man development and roster construction.