import streamlit as st
import pandas as pd

def render_sidebar_filters(data):
    st.sidebar.header("Filters")
    all_years = sorted(set(data["team"]["Year"].dropna().astype(int).tolist()) | set(data["players"]["Year"].dropna().astype(int).tolist()))
    year_range = st.sidebar.slider("Year range", min_value=min(all_years), max_value=max(all_years), value=(min(all_years), max(all_years)), step=2)
    conferences = ["All"] + sorted([c for c in data["team"]["Conference"].dropna().unique().tolist()])
    conference = st.sidebar.selectbox("Conference", conferences, index=0)
    teams = sorted(data["team"]["TeamAbv"].dropna().unique().tolist())
    selected_teams = st.sidebar.multiselect("Teams", teams, default=[])
    players = sorted(data["players"]["Player"].dropna().unique().tolist())
    default_players = [p for p in ["Dirk Nowitzki", "Brook Lopez", "Joel Embiid", "Shaquille O'Neal"] if p in players]
    selected_players = st.sidebar.multiselect("Players", players, default=default_players)
    positions = ["Both"] + sorted(data["players"]["Pos"].dropna().unique().tolist())
    position = st.sidebar.selectbox("Player position", positions, index=0)
    return {
        "year_range": year_range,
        "conference": conference,
        "teams": selected_teams,
        "players": selected_players,
        "position": position,
    }

def apply_team_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    out = df[(df["Year"] >= filters["year_range"][0]) & (df["Year"] <= filters["year_range"][1])].copy()
    if filters["conference"] != "All":
        out = out[out["Conference"] == filters["conference"]]
    if filters["teams"]:
        out = out[out["TeamAbv"].isin(filters["teams"])]
    return out

def apply_player_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    out = df[(df["Year"] >= filters["year_range"][0]) & (df["Year"] <= filters["year_range"][1])].copy()
    if filters["players"]:
        out = out[out["Player"].isin(filters["players"])]
    if filters["position"] != "Both":
        out = out[out["Pos"] == filters["position"]]
    return out