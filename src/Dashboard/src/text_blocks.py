import streamlit as st

def intro_text():
    return """
This dashboard is built from your cleaned NBA datasets to help answer a decision-support question:
**How important has three-point shooting from power forwards and centers become for team success and player value?**

Use the filters in the sidebar to move across eras, isolate teams or conferences, and compare how individual PF/C players adapted to the growing role of the three-point shot.
"""

def decision_text():
    return """
The dashboard suggests that PF/C shot selection has clearly shifted over time, with three-point attempts becoming a much larger part of frontcourt offense than they were in earlier eras.
At the team level, the success scatterplot lets the decision-maker test whether heavier PF/C perimeter involvement tends to line up with more wins or a stronger winning percentage.
At the player level, the adaptation chart shows that this change was uneven: some big men remained almost entirely interior scorers, while others evolved into clear perimeter threats.

Taken together, the evidence points toward a modern NBA environment in which PF/C shooting versatility is more strategically valuable than it once was.
That does not mean three-point shooting alone determines team success, but it does mean frontcourt perimeter skill now deserves meaningful weight in roster evaluation, player development, and team construction decisions.
"""
def render_how_to_page():
    with st.expander("How to use this Dashboard", expanded=True):
        st.markdown("""
### How to Use This Dashboard

This dashboard is designed to help the viewer explore how power forwards and centers have changed as three-point shooting became a larger part of the NBA.

Use the filters on the sidebar or within each chart to focus on specific years, teams, players, or shooting statistics. The dashboard is interactive, so changing a filter will update the visualizations automatically.

#### What each section does

**League Trends**  
This section shows how PF/C shot selection has changed over time across the league. You can use it to compare how much frontcourt players relied on two-point and three-point shooting in different years.

**Team Success**  
This section explores the relationship between PF/C shooting and team performance. Use the filters to examine whether teams with more shooting from their big men also tended to win more games.

**Player Adaptation Over Time**  
This section lets you compare selected players and see how they adapted over their careers. You can switch between different shooting statistics to track changes in shot attempts, makes, and efficiency.

#### How to read the dashboard

Start with the league-wide trends to understand the overall shift in the game. Then move to the team success section to see whether that shift appears to connect with winning. Finally, use the player section to look at how individual PF/C players adapted differently across eras.

#### Notes

The data is organized by available seasons in the cleaned dataset, and some player shooting files are recorded in two-year intervals. Because of that, some views may not include every single season from 1990 to 2025.

This dashboard is meant to support the decision question by showing how the changing offensive role of PF/C players may relate to modern team success and player value.
        """)
        