"""
GeoSaarthi - Member 3 (GIS/Routing/App) - Day 1-2 Practice
=============================================================
GOAL: Get a Streamlit + Folium map of Assam rendering on screen.
This derisks your trickiest install (Streamlit/Folium/GeoPandas)
early, before real road/population/shelter data arrives.

Run this in Anaconda Prompt with:
    conda activate geosaarthi
    streamlit run member3_assam_map_starter.py

(It will open a browser tab automatically.)
"""

import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="GeoSaarthi - Assam Map Prototype", layout="wide")

st.title("GeoSaarthi - Day 1-2 Map Prototype")
st.caption("This is a placeholder map. Real flood risk, roads, and shelter "
           "layers get added in Week 2-3.")

# Rough center coordinates of Assam
ASSAM_CENTER = [26.2006, 92.9376]

# -------------------------------------------------------------
# STEP 1: Sidebar controls (this becomes your "what-if" scenario
# panel later - rainfall slider, temperature slider, etc.)
# -------------------------------------------------------------
st.sidebar.header("Scenario Controls (placeholder)")
rainfall_increase = st.sidebar.slider("Rainfall change (%)", -50, 100, 0, step=10)
st.sidebar.write(f"Selected scenario: {rainfall_increase:+d}% rainfall")

# -------------------------------------------------------------
# STEP 2: Fake shelter points (swap for real shelter CSV later)
# -------------------------------------------------------------
fake_shelters = pd.DataFrame({
    "name": ["Shelter A", "Shelter B", "Shelter C"],
    "lat": [26.18, 26.25, 26.10],
    "lon": [92.90, 93.05, 92.80],
    "capacity": [200, 150, 300],
})

# -------------------------------------------------------------
# STEP 3: Build the Folium map
# -------------------------------------------------------------
m = folium.Map(location=ASSAM_CENTER, zoom_start=8, tiles="OpenStreetMap")

# Mark Assam's rough center
folium.Marker(
    ASSAM_CENTER,
    popup="Assam (study area center)",
    icon=folium.Icon(color="blue"),
).add_to(m)

# Add placeholder shelters
for _, row in fake_shelters.iterrows():
    folium.Marker(
        [row["lat"], row["lon"]],
        popup=f"{row['name']} (capacity: {row['capacity']})",
        icon=folium.Icon(color="green", icon="home"),
    ).add_to(m)

# A placeholder "risk zone" circle - this is where your real
# flood-risk GeoJSON polygon will go in Week 2-3
# Circle radius now grows with the rainfall scenario slider
base_radius = 8000
scenario_radius = base_radius * (1 + rainfall_increase / 100)

folium.Circle(
    location=[26.15, 92.95],
    radius=scenario_radius,
    color="red",
    fill=True,
    fill_opacity=0.2,
    popup=f"Placeholder flood risk zone ({rainfall_increase:+d}% scenario)",
).add_to(m)

# -------------------------------------------------------------
# STEP 4: Render in Streamlit
# -------------------------------------------------------------
col1, col2 = st.columns([3, 1])
with col1:
    st_folium(m, width=900, height=550)
with col2:
    st.metric("Population at risk (placeholder)", "12,400")
    st.metric("Shelters shown", len(fake_shelters))
    st.info("Next: replace placeholder shelter/risk data with real "
            "OSM roads + population + shelter datasets.")