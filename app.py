import streamlit as st
import pandas as pd
from geolocation import get_ip_based_location
from streamlit_javascript import st_javascript
client_ip = st_javascript("await fetch('https://api.ipify.org').then(r=>r.text())")

st.write("Client IP address:")
st.write(client_ip)

st.write("Hello world")

ip = st.context.headers.get("x-forwarded-for")

# Fetch location based on IP address
location = get_ip_based_location(ip)
if "error" in location:
    st.error(f"Error fetching location: {location['error']}")

st.write("Your location based on IP address:")
st.write(location)

if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ":" in ip:
    st.write("You have an IPv6 address.", ip)
elif "." in ip:
    st.write("You have an IPv4 address.", ip)
else:
    st.error("This should not happen.")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))