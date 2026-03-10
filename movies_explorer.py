import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("movies_cleaned.csv")

# Title
st.title("Movie Explorer App")

# Extract all unique genres
all_genres = sorted(
    {genre for genres in df["genres"] for genre in genres.split("|")}
)

# Selectbox (one genre only)
selected_genre = st.selectbox("Select a genre:", all_genres)

# Filter movies containing the selected genre
filtered_movies = df[df["genres"].str.contains(selected_genre)]

# Display table
st.subheader(f"Movies in Genre: {selected_genre}")
st.dataframe(filtered_movies[["title", "genres", "year"]])
