# Final Project - Examining Tornado Occurences in the Carolinas (1950-2023)
My final project examining tornado distribution and their impacts across the Carolinas using data from the Storm Prediction Center

## Storm Prediction Center - Tornado Records

INTRODUCTION: The primary goal of this project is to create an easy to use application to view tornado statistics and visuals for North and South Carolina.

DATA/DESIGN: The data set used for this project comes from the Storm Prediction Center (SPC) dataset containing all recorded tornado records in the US from 1950-2023. The data was filtered for just NC & SC, and I removed any tornadoes that had not recieved a rating (approx 3-5 records from the last few years). Originally I wanted to have a variety of charts that could be sorted with drop down menus and spread throughout multiple pages for users to explore these tornado records. However, I ended up using the mapping feature and tooltips as the primary way to view this info. The tracks are color coded, and the tool tip provides the time of the tornado, number of fatalities, magnitude (on the Fujita or Enhanced Fujita Scale - F/EF), distance traveled (miles) and max width (yards) if available. Lastly, I provided some line charts for users to be able to get a quick glance at what years had major spikes in tornadoes and fatalities. This can then be used to further explore the maps page. 

FUTURE WORK: I believe there are some really unique charts I could continue to build on the "chart facts" page. Additionally, I was unable to get the session state to hold in place the selection on the chart facts page, however it works perfectly on the maps page where most of the information is gained. Adding figures or buckets that show the amount of damage caused would also be a great feature to add. I believe adding climate state info (ENSO, etc) would also be a great layer to add to see if there are any large scale patterns we could identify that possibly result in increased tornado frequency in the Carolinas. 

View my Tableau Dashboard at this Link: [https://final-project-carolina-tornadoes.streamlit.app/]

Data Source Link: [https://www.spc.noaa.gov/wcm/#data]
