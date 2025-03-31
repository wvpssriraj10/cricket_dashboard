import streamlit as st
import pandas as pd

batting_df = pd.read_csv("player_batting_stats.csv")
bowling_df = pd.read_csv("player_bowling_stats.csv")

st.title("🏏 Cricket Player Dashboard")

player_name = st.text_input("Enter Player Name:", "")

if player_name:
    batting_stats = batting_df[batting_df["Player"] == player_name]
    bowling_stats = bowling_df[bowling_df["Player"] == player_name]

    if not batting_stats.empty:
        st.subheader("Batting Stats")
        st.dataframe(batting_stats)

    if not bowling_stats.empty:
        st.subheader("Bowling Stats")
        st.dataframe(bowling_stats)

    if batting_stats.empty and bowling_stats.empty:
        st.warning("No records found for this player.")
