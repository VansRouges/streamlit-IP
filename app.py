import streamlit as st
import pandas as pd
from geolocation import get_ip_based_location
from streamlit_javascript import st_javascript
client_ip = st_javascript("await fetch('https://api.ipify.org').then(r=>r.text())")

st.write("Client IP address:")
st.write(client_ip)

st.write("Hello world")

ip = st.context.ip_address
st.write(ip)

# Fetch location based on IP address
location = get_ip_based_location(client_ip)
if "error" in location:
    st.error(f"Error fetching location: {location['error']}")

st.write("Your location based on IP address:")
st.write(location)

st.html(
    """
    <style>
        .custom-card {
            background: #f9f9f9;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07);
            padding: 24px;
            margin-bottom: 16px;
            max-width: 400px;
        }
        .custom-title {
            color: #e74c3c;
            margin-top: 0;
        }
        .custom-paragraph {
            color: #2c3e50;
            font-size: 16px;
        }
        .custom-strike {
            text-decoration: line-through double red;
        }
        .custom-button {
            background: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            cursor: pointer;
            font-size: 16px;
        }
        .ip-address {
            font-weight: bold;
            color: #27ae60;
            margin-top: 12px;
            display: block;
        }
    </style>
    <div class="custom-card">
        <h2 class="custom-title">Welcome!</h2>
        <p class="custom-paragraph">
            <span class="custom-strike">Oops</span>! 
            This is a <b>custom HTML card</b> with <span style='color: #3498db;'>CSS styling, bruh</span>.
        </p>
        <button class="custom-button">Click Me</button>
        <span id="ip" class="ip-address"></span>
    </div>
    <script>
        fetch('https://ipinfo.io/json')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ip').textContent = "Your IP: " + data.ip;
            })
            .catch(error => {
                document.getElementById('ip').textContent = "Error fetching IP";
            });
    </script>
    """
)

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