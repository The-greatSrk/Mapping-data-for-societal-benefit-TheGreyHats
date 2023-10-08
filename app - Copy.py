python
import folium
import pandas as pd

# Load the data
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.csv'
states = pd.read_csv(url)

# Create the map
map = folium.Map(location=[48, -102], zoom_start=4)

# Add the data to the map
for i in range(0, len(states)):
    folium.Marker([states.iloc[i]['LAT'], states.iloc[i]['LON']], popup=states.iloc[i]['NAME']).add_to(map)

# Save the map
map.save('us_states_map.html')