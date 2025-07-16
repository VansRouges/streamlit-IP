import streamlit as st

st.write("Hello world")

ip = st.context.ip_address
if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ip.contains(":"):
    st.write("You have an IPv6 address.", ip)
elif ip.contains("."):
    st.write("You have an IPv4 address.", ip)
else:
    st.error("This should not happen.")