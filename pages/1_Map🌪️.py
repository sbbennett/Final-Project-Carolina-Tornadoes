import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Caching the Data
@st.cache_data
def load_data():
    Tornado_Data = pd.read_csv('tornado.csv')
    return Tornado_Data

st.set_page_config(layout="wide")

# Streamlit app title
st.title("Tornadoes by Year in the Carolinas 1950-2023")

#Quick note on why it defaults to 2011
st.write("**Use the sliding bar or the prev/next year buttons to change the year. Then, hover your mouse over the tornado track or point to view data on the tornado.**")

# Load cached data
data = load_data()

# Filter for NC and SC tornadoes
df_filtered = data[data["st"].isin(["NC", "SC"])]

# Initialize session state for start and end years
if "selected_year" not in st.session_state:
    # Set default to 2011, but ensure it's within the dataset's range
    st.session_state["selected_year"] = 2011 if 2011 in data["yr"].values else int(data["yr"].min())

# Layout for the year slider and buttons
col1, col2, col3 = st.columns([1, 6, 1])  # Adjust column widths for layout

with col1:
    if st.button("⬅️ Prev. Year"):
        if st.session_state["selected_year"] > int(data["yr"].min()):
            st.session_state["selected_year"] -= 1

with col2:
    selected_year = st.slider(
        "Select Year",
        int(data["yr"].min()),  # Minimum year
        int(data["yr"].max()),  # Maximum year
        st.session_state["selected_year"]  # Default value from session state
    )

# Update session state with slider value
st.session_state["selected_year"] = selected_year

with col3:
    if st.button("Next Year ➡️"):
        if st.session_state["selected_year"] < int(data["yr"].max()):
            st.session_state["selected_year"] += 1

# Filter the dataset by the selected year
df_filtered = data[
    (data["st"].isin(["NC", "SC"])) & 
    (data["yr"] == st.session_state["selected_year"])
]

# Display a summary
st.write(f"Tornadoes in {st.session_state['selected_year']}: {len(df_filtered)}")

# Create a map centered on the average latitude and longitude
center_lat = df_filtered["slat"].mean()
center_lon = df_filtered["slon"].mean()
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=7)

# Add tornado points to the map
magnitude_colors = {
    0: "blue",
    1: "green",
    2: "yellow",
    3: "red",
    4: "purple"
}

for _, row in df_filtered.iterrows():
    if row["elat"] != 0 and row["elon"] != 0:  # Check if end location exists
        # Calculate path distance in miles and width in yards
        path_distance_miles = row["len"]  # 'len' is in miles
        path_width_yards = row["wid"]  # 'wid' is in yards

        # Format the tooltip
        tooltip = (
            f"Tornado Path<br>"
            f"Date: {row['date']}<br>"
            f"Time: {row['time']}<br>"
            f"Magnitude: {row['mag']}<br>"
            f"Path Distance: {path_distance_miles} miles<br>"
            f"Path Width: {path_width_yards} yards<br>"
            f"Injuries: {row['inj']}<br>"
            f"Fatalities: {row['fat']}"
        )

        # Add a line from the start to the end location
        folium.PolyLine(
            locations=[(row["slat"], row["slon"]), (row["elat"], row["elon"])],
            color=magnitude_colors.get(row["mag"], "gray"),
            weight=5,  # Line thickness
            tooltip=tooltip
        ).add_to(mymap)
    else:
        # Fallback for tornadoes with no end location
        color = magnitude_colors.get(row["mag"], "gray")
        tooltip = (
            f"Tornado on {row['date']} at {row['time']}<br>"
            f"Magnitude: {row['mag']}<br>"
            f"Injuries: {row['inj']}<br>"
            f"Fatalities: {row['fat']}"
        )
        folium.CircleMarker(
            location=[row["slat"], row["slon"]],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            tooltip=tooltip
        ).add_to(mymap)

# Define the color map for tornado magnitudes
color_map = {
    "F/EF0": "blue",
    "F/EF1": "green",
    "F/EF2": "yellow",
    "F/EF3": "red",
    "F/EF4": "purple",
}

col1, col2 = st.columns([4, 1])  # Adjust column width ratio as needed

# Add the map to the left column
with col1:
    st.write("Tornado Map:")
    st_folium(mymap, width=700, height=500)

# Add the legend to the right column
with col2:
    st.write("Legend:")
    for category, color in color_map.items():
        st.markdown(
            f"- {category}: <span style='color:{color}; font-size:20px;'>●</span>",
            unsafe_allow_html=True
        )


st.write("The above map displays the tracks of tornadoes where the start and end locations are known. If no end location is known, then just the starting or reporting location is shown. The tracks and points are color coded to the magnitude of the tornado according to the Fujita (F) or Enhanced Fujita (EF) Scale. The rating of the tornadoes ranges from the weakest of F/EF0, increasing in strength through F/EF1, F/EF2, F/EF3, and F/EF4. North and South Carolina have had no recorded F/EF5 tornadoes as of December 2024 when this project was made.")
