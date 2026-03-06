# Background

Over the past three decades, the NBA has undergone a significant transformation in offensive strategy and player roles. In earlier eras of professional basketball, power forwards and centers were primarily responsible for interior play. These players typically focused on scoring near the basket, securing rebounds, and protecting the rim on defense. Offensive systems often revolved around post play, and perimeter shooting from frontcourt players was relatively rare. However, the structure of NBA offenses has gradually shifted toward greater emphasis on spacing, ball movement, and three-point shooting.

The increasing importance of three-point shooting has influenced how teams use players across all positions, including power forwards and centers. As perimeter shooting has become a central component of modern offenses, some frontcourt players have adapted by expanding their shooting range. These players, often referred to as “stretch bigs,” are capable of shooting from beyond the three-point line while still providing many of the traditional responsibilities of a big man. Stretch bigs can create spacing for teammates, pull opposing defenders away from the paint, and contribute to offensive versatility.

The emergence of stretch bigs has raised an important strategic question for NBA teams. Front offices and coaching staffs must decide whether three-point shooting should now be considered a required skill for frontcourt players. While perimeter shooting offers advantages such as improved spacing and offensive flexibility, traditional big men can still provide valuable skills including rebounding, interior scoring, and rim protection. Teams must balance these competing priorities when constructing their rosters and designing player development programs.

Understanding how the role of power forwards and centers has evolved is therefore critical for making informed roster decisions. If frontcourt players are increasingly expected to contribute as perimeter shooters, teams may benefit from prioritizing shooting ability when scouting, drafting, and developing big men. On the other hand, if interior skills remain equally or more important, organizations may choose to maintain a more traditional approach to frontcourt player development.

This project aims to examine whether the role of NBA power forwards and centers has shifted toward perimeter shooting over the past thirty years. Using a compiled dataset of frontcourt shooting statistics across multiple seasons, the analysis investigates long-term trends in shot selection. By examining changes in three-point attempts and other shooting metrics, the project seeks to determine whether frontcourt players are increasingly contributing as perimeter shooters.

The findings of this analysis will help inform the strategic decision faced by NBA teams regarding frontcourt player development and roster construction. If clear evidence shows that perimeter shooting among big men has increased significantly over time, this would support the argument that three-point shooting should be incorporated as a core skill in modern frontcourt development. Conversely, if the data suggests that interior play remains dominant, teams may continue prioritizing traditional big-man skills.

Ultimately, this project aims to provide data-driven insight into how the role of NBA big men has evolved and what that evolution means for future roster construction and player development strategies.

## Decision Maker

• NBA General Manager

◦ Has authority over roster construction, draft strategy, and player acquisition
◦ Determines player development priorities within the organization
◦ Makes long-term strategic decisions about team play style and roster composition
◦ Operates under real constraints (salary cap, draft assets, player availability, and competitive pressure)

• Brad Stevens – President of Basketball Operations, Boston Celtics

Brad Stevens oversees basketball operations for the Boston Celtics and is responsible for roster construction, player development priorities, and long-term strategic direction. Executives in this role must decide whether modern frontcourt players should be developed primarily as traditional interior big men or as “stretch bigs” capable of contributing as perimeter shooters.

## Key Stakeholders

• Head Coach (NBA Team) – Responsible for implementing offensive systems and determining how frontcourt players are used within the team’s strategy.

• Director of Player Development – Oversees training programs and skill development for players, including whether shooting becomes a required skill for power forwards and centers.

• Frontcourt Players (Power Forwards and Centers) – Their skill development, role expectations, and career opportunities are directly affected by how teams value perimeter shooting.

• Team Ownership – Interested in team success, competitive advantage, and the long-term strategic direction of the organization.

• Fans and Analysts – Influence public perception of roster decisions and strategic approaches to modern basketball.

## Planned Data-Sets:

#### NBA Yearly Summary for Power Forwards

This dataset contains aggregated yearly shooting statistics for NBA power forwards from 1990 to 2024. The data was constructed using season-level player statistics from the Basketball-Reference database. Player totals were collected for each NBA season and filtered to include only players whose primary position was power forward.

Using Python scripts, the player-level data was cleaned and aggregated into yearly summaries. The data preparation process included removing unnecessary columns, standardizing season formats, converting season labels from “YYYY–YY” to a single starting year, and calculating yearly averages and totals for key shooting metrics. These metrics include three-point attempts (3PA), three-point makes (3P), two-point attempts (2PA), two-point makes (2P), and shooting percentages.

This dataset allows the project to examine long-term trends in frontcourt shot selection and determine whether power forwards have increasingly incorporated three-point shooting into their offensive role over time.

#### NBA Team Power Forward and Center Shooting Data (Yearly)

This dataset compiles team-level shooting statistics for power forwards and centers across all NBA teams from 1990 to 2024. The dataset was constructed by combining multiple season-level CSV files containing player shooting statistics for frontcourt positions.

The data was processed using Python scripts in Visual Studio Code to automate the cleaning and aggregation process. These scripts searched through multiple CSV files, standardized historical team abbreviations (for example Seattle to Oklahoma City and New Jersey to Brooklyn, etc.), and merged the datasets into a single consistent format. The scripts also calculated team-level averages and totals for shooting metrics including three-point attempts, two-point attempts, field goal percentages, and other relevant statistics.

Additional processing steps included removing redundant variables, standardizing column names, and generating totals for shot attempts by power forwards and centers on each team. The resulting dataset provides a consistent 30-year record of how frontcourt shooting behavior has evolved at the team level. This dataset will be used to evaluate whether perimeter shooting has become a common expectation for modern NBA big men.

#### NBA Team Success (Win–Loss Records)

This dataset contains yearly team performance metrics for NBA teams from 1990 to 2024, including wins, losses, and overall team success indicators. The data was collected from Basketball-Reference team statistics and organized into a structured dataset covering the same time period as the frontcourt shooting data.

The dataset was cleaned using Python to standardize team names and abbreviations so that they match the team identifiers used in the shooting datasets. Historical franchise changes and relocations were also normalized to ensure consistency across seasons.

This dataset allows the project to examine potential relationships between frontcourt shooting trends and team success. By combining team performance data with frontcourt shooting statistics, the analysis can explore whether teams that incorporate perimeter shooting from power forwards and centers tend to achieve stronger competitive outcomes.

#### Data Wrangling Overview

To prepare the datasets used in this project, several Python scripts were developed in Visual Studio Code to automate data cleaning and aggregation tasks. The original player statistics were downloaded as season-level CSV files containing shooting data for NBA players. These files were then processed using Python’s CSV and file-handling libraries to create consistent datasets suitable for long-term analysis.

The wrangling process included filtering the data to include only power forwards and centers, merging multiple season files into unified datasets, and calculating yearly and team-level statistics. Several data standardization steps were required to ensure consistency across seasons, including correcting historical team abbreviations, merging team city and team name fields, removing redundant columns, and converting season labels from “YYYY–YY” format to a single starting year.

Additional scripts were used to compute team-level averages and totals for frontcourt shooting statistics and to create summary datasets that capture long-term trends in shot selection. These automated scripts allow the entire dataset to be reproduced if new seasons are added in the future.

Together, these data wrangling steps produced a clean, consistent dataset covering approximately 30 years of NBA frontcourt shooting behavior, enabling the project to analyze how the role of power forwards and centers has evolved and how these changes may influence roster construction decisions.

### Citations APA

Basketball-Reference. (2025). NBA player totals statistics (1990–2024 seasons). Sports Reference LLC. https://www.basketball-reference.com/leagues/NBA_2025_totals.html

National Basketball Association. (2024). NBA statistics. https://stats.nba.com

#### Note:

I used the data from basketball reference, bi-annually from 1990-2024 as to mitigate the length of time it would take to assemble over 30 datasets. (this way the data is still consistent and correct, but it takes less time to clean) Using VS-Code I created a python program that would clean the data, make additions/removals, organize all the player stats and totals from Basketball reference to only include data belonging to the Power-Forward (PF) and Center (C) positions. The other changes made were mostly for data consistency such as seasons instead of years as tableau cannot read a year presented as XXXX-XX (Season) so I changed them to the year that the season began, and other issues regarding consistency such as Teams either switching names or cities or in some cases both. 