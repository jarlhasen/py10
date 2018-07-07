import folium

# we can get cordinates of the place by google map
# open google map and then right click and then chose what's there?
map = folium.Map(location=[38.8,-99.09],zoom_start=6, tiles="Mapbox Bright") # pass a list of cordinate of the location
map