import streamlit as st
from src.data_loader import load_data
from src.filters import render_sidebar_filters, apply_team_filters, apply_player_filters
from src.charts import league_trend_chart, team_success_scatter, player_adaptation_chart, top_teams_bar_chart
from src.text_blocks import intro_text, decision_text, render_how_to_page 

st.set_page_config(page_title="PF/C 3PT Evolution Dashboard", layout="wide")
st.title("NBA PF/C Three-Point Evolution Dashboard")
st.markdown(intro_text())
render_how_to_page()

data = load_data()
filters = render_sidebar_filters(data)

tab1, tab2, tab3 = st.tabs(["League Trends", "Team Success", "Player Adaptation"])

with tab1:
    st.subheader("League-wide PF/C shot profile over time")
    metric_mode = st.radio("Choose trend view", ["Attempts", "Makes", "Percentages"], horizontal=True, key="trend_mode")
    fig1 = league_trend_chart(data["yearly"], metric_mode, filters["year_range"])
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown(
        "This view helps the decision-maker see how PF/C roles changed over time. "
        "Your cleaned PF/C summary is available in two-year intervals, so the timeline reflects that structure."
    )

    st.subheader("Top teams by PF/C perimeter usage")
    year_options = sorted(data["team"]["Year"].dropna().astype(int).unique().tolist())
    year_for_bar = st.selectbox("Pick a year for team comparison", year_options, index=len(year_options)-1)
    fig_bar = top_teams_bar_chart(data["team"], year_for_bar)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("This view highlights which teams leaned most heavily into PF/C three-point volume in a selected season.")

with tab2:
    st.subheader("Team success vs PF/C three-point involvement")
    team_filtered = apply_team_filters(data["team"], filters)
    c1, c2 = st.columns(2)
    with c1:
        y_metric = st.selectbox("Y-axis metric", ["W", "W_PCT"], index=1)
    with c2:
        x_metric = st.selectbox("X-axis metric", ["3PA", "3P%", "TOTAL_3PA", "TOTAL_3P"], index=0)
    fig2 = team_success_scatter(team_filtered, x_metric, y_metric)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown(
        "This scatterplot is framed as decision support: it tests whether stronger PF/C perimeter volume or efficiency lines up with stronger team results."
    )

with tab3:
    st.subheader("How selected PF/C players adapted over time")
    player_filtered = apply_player_filters(data["players"], filters)
    player_metric = st.selectbox("Player metric", ["3PA", "3P", "3P%", "2PA", "2P%"], index=0)
    fig3 = player_adaptation_chart(player_filtered, player_metric)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown(
        "This view connects the league trend back to real players and shows that some frontcourt players adapted far more than others."
    )

st.markdown("---")
st.subheader("Implications for the Decision")
st.markdown(decision_text())
