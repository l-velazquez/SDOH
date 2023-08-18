import folium
import streamlit as st

m = folium.Map()

folium.Marker([0, 0]).add_to(m)

# Display map using folium's built-in method
m.add_to(st.empty())

# Display using st.write
st.write(m)