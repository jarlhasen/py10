import folium
# we can get cordinates of the place by google map
# open google map and then right click and then chose what's there?
map = folium.Map(location=[38.8,-99.09],zoom_start=6, tiles="Mapbox Bright") # pass a list of cordinate of the location
# how to add points to this map?
map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a marker",icon=folium.Icon(color='green')))
map.save("m.html")