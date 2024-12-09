# Windows
# python -m venv venv
# venv\Scripts\activate.bat

import streamlit as st

st.set_page_config(layout="wide")

st.markdown('---')
st.header("An Exploration of :red[Tornadoes] in NC & SC")

col1, col2 = st.columns(2)

# Add the first image to the first column
with col1:
    st.image("Images/nc_tornado.jpg", width=500)

# Add the second image to the second column
with col2:
    st.image("Images/tornado_warnings.png", width=500)


st.write("North Carolina and South Carolina are no strangers to tornadoes, with a few notable outbreaks and strong tornadoes striking the states over the last 70 or so years. Additionally, the frequency of hurricanes and tropical storms striking the states also bring an increased risk of tornadoes in the summer and early fall. The Storm Predicition Center, also known as the **SPC**, is the main forecasting agency responsible for forecasting severe thunderstorms and tornado outbreaks. The necessary local National Weather Service offices will survey and rate any tornado reports that occur in their regions. These reports are logged and stored by the SPC, and this is where we have pulled our data from. **This Data Set spans 1950-2023**")

st.header("What is the :red[goal] of this Project?")
st.write("The primary goal of this project is to create an easy to use application to view tornado statistics and visuals for North and South Carolina.")

st.header("How Does this App Work?")
st.write("Click on the page to the left that says Map. From there, you can filter by individual years and see where and when a tornado occurred, it's path (if available), rating, time, max length (miles) and width (yards), and how many fatalities it caused. Major years to explore are **1984, 1988, 1989, 1992, 2008, 2011, and 2020**.  Finally, I have included some line charts on the Chart Facts page showing total tornadoes and tornado fatalities per year. Use the drop down menus to choose between state and measures.")
