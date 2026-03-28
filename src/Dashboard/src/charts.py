import pandas as pd
import plotly.express as px

def league_trend_chart(df: pd.DataFrame, metric_mode: str, year_range: tuple):
    out = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])].copy()
    if metric_mode == "Attempts":
        plot_df = out.melt(id_vars="Year", value_vars=["TOTAL_2PA", "TOTAL_3PA"], var_name="Metric", value_name="Value")
        title = "Total PF/C shot attempts over time"
    elif metric_mode == "Makes":
        plot_df = out.melt(id_vars="Year", value_vars=["TOTAL_2P", "TOTAL_3P"], var_name="Metric", value_name="Value")
        title = "Total PF/C made shots over time"
    else:
        plot_df = out.melt(id_vars="Year", value_vars=["2P%", "3P%"], var_name="Metric", value_name="Value")
        title = "PF/C efficiency over time"
    fig = px.line(plot_df, x="Year", y="Value", color="Metric", markers=True, title=title)
    fig.update_layout(xaxis_title="Year", yaxis_title="Value", legend_title="")
    return fig

def top_teams_bar_chart(df: pd.DataFrame, year: int):
    out = df[df["Year"] == year].nlargest(10, "TOTAL_3PA").copy()
    fig = px.bar(
        out.sort_values("TOTAL_3PA"),
        x="TOTAL_3PA",
        y="TeamAbv",
        orientation="h",
        hover_data=["TeamName", "W", "W_PCT"],
        title=f"Top 10 teams by PF/C total 3PA in {year}"
    )
    fig.update_layout(xaxis_title="PF/C Total 3PA", yaxis_title="Team")
    return fig

def team_success_scatter(df: pd.DataFrame, x_metric: str, y_metric: str):
    fig = px.scatter(
        df,
        x=x_metric,
        y=y_metric,
        hover_name="TeamName",
        hover_data=["Year", "Conference", "TeamAbv"],
        trendline="ols",
        title=f"{y_metric} vs {x_metric}"
    )
    fig.update_layout(xaxis_title=x_metric, yaxis_title=y_metric)
    return fig

def player_adaptation_chart(df: pd.DataFrame, metric: str):
    if df.empty:
        fig = px.line(title="No players match the current filters")
        return fig
    fig = px.line(
        df.sort_values(["Player", "Year"]),
        x="Year",
        y=metric,
        color="Player",
        markers=True,
        hover_data=["Team", "Pos", "Age"],
        title=f"Selected PF/C players: {metric} over time"
    )
    fig.update_layout(xaxis_title="Year", yaxis_title=metric, legend_title="")
    return fig
