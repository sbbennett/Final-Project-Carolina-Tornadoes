import streamlit as st
import pandas as pd
import altair as alt

# Caching the Data
@st.cache_data
def load_data():
    return pd.read_csv('tornado.csv')

st.set_page_config(layout="wide")

# Load cached data
data = load_data()

# Ensure columns are numeric
data["yr"] = pd.to_numeric(data["yr"], errors="coerce")
data["mag"] = pd.to_numeric(data["mag"], errors="coerce")

# Initialize session state for state selection
if "selected_state" not in st.session_state:
    st.session_state["selected_state"] = "NC"

# Dropdown menu to select a state (with session state)
state = st.selectbox("Select State", ["NC", "SC"], key="selected_state")

# Filter data for the selected state
filtered_data = data[data["st"] == st.session_state["selected_state"]]

# Compute yearly tornado counts
tornadoes_per_year = (
    filtered_data.groupby("yr").size().reset_index(name="Total Tornadoes")
)

# Compute yearly tornado fatalities
fatalities_per_year = (
    filtered_data.groupby("yr")["fat"].sum().reset_index(name="Total Fatalities")
)

# Store computed data in session state
if "tornado_charts_data" not in st.session_state:
    st.session_state["tornado_charts_data"] = {}

st.session_state["tornado_charts_data"][state] = {
    "tornadoes_per_year": tornadoes_per_year,
    "fatalities_per_year": fatalities_per_year,
}

# Dropdown menu to select a chart type
chart_type = st.selectbox(
    "Select Chart Type",
    ["Total Tornadoes Per Year", "Tornado Fatalities Per Year"]
)

# Retrieve data for charts
charts_data = st.session_state["tornado_charts_data"][state]

# Display the selected chart
st.subheader(f"Tornado Data for {state} - {chart_type}")

if chart_type == "Total Tornadoes Per Year":
    tornado_chart = alt.Chart(charts_data["tornadoes_per_year"]).mark_line(point=True).encode(
        x=alt.X("yr:O", title="Year"),
        y=alt.Y("Total Tornadoes:Q", title="Number of Tornadoes"),
        tooltip=["yr", "Total Tornadoes"]
    ).properties(width=700, height=400)
    st.altair_chart(tornado_chart)

elif chart_type == "Tornado Fatalities Per Year":
    fatalities_chart = alt.Chart(charts_data["fatalities_per_year"]).mark_line(point=True).encode(
        x=alt.X("yr:O", title="Year"),
        y=alt.Y("Total Fatalities:Q", title="Number of Fatalities"),
        tooltip=["yr", "Total Fatalities"]
    ).properties(width=700, height=400)
    st.altair_chart(fatalities_chart)
