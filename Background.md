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

### References

Basketball-Reference. (2025). NBA player totals statistics (1990–2024 seasons). Sports Reference LLC. https://www.basketball-reference.com/leagues/NBA_2025_totals.html

National Basketball Association. (2024). NBA statistics. https://stats.nba.com

#### Note:

I used the data from basketball reference, bi-annually from 1990-2024 as to mitigate the length of time it would take to assemble over 30 datasets. (this way the data is still consistent and correct, but it takes less time to clean) Using VS-Code I created a python program that would clean the data, make additions/removals, organize all the player stats and totals from Basketball reference to only include data belonging to the Power-Forward (PF) and Center (C) positions. The other changes made were mostly for data consistency such as seasons instead of years as tableau cannot read a year presented as XXXX-XX (Season) so I changed them to the year that the season began, and other issues regarding consistency such as Teams either switching names or cities or in some cases both. 