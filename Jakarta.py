import folium

pebridayanti = folium.Map (
    location=[-6.223564, 106.910794], 
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'




folium.Marker([-6.186491, 106.834086], popup='<i>Super indo marakas </i>').add_to(pebridayanti)
folium.Marker([-6.190285, 106.838792], popup='<i>Taman Ismail Marzuki</i>').add_to(pebridayanti)
folium.Marker([-6.192381, 106.818611], popup='<i>Kb.Kacang</i>').add_to(pebridayanti)
folium.Marker([-6.178431, 106.811987], popup='<i>Cideng</i>').add_to(pebridayanti)
folium.Marker([-6.183848, 106.836464], popup='<i>Kwitang</i>').add_to(pebridayanti)
folium.Marker([-6.203986, 106.848823], popup='<i>Pegangsaan</i>').add_to(pebridayanti)
folium.Marker([-6.194941, 106.845219], popup='<i>Kenari</i>').add_to(pebridayanti)
folium.Marker([-6.261920, 106.831258], popup='<i>Kalibata</i>').add_to(pebridayanti)
folium.Marker([-6.223247, 106.911958], popup='<i>12</i>').add_to(pebridayanti)
folium.Marker([-6.223487, 106.910783], popup='<i>Jl.Duren Sawit Indah Bblok A7 No.4</i>').add_to(pebridayanti)