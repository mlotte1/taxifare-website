import streamlit as st
import requests
from datetime import datetime

st.title("Taxi Fare Prediction")

st.markdown("### Enter Ride Details")

pickup_date = st.date_input("Pickup Date")
pickup_time = st.time_input("Pickup Time")
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Number of Passengers", min_value=1)



url = 'https://taxifare.lewagon.ai/predict'

pickup_datetime = f"{pickup_date} {pickup_time}"

payload = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

st.markdown("## Estimation")

response = requests.get(url, params=payload)

if response.status_code == 200:
    result = response.json()
    fare = result.get('fare')

    if fare is not None:
        st.write(f"The predicted fare is: ${fare:.2f}")
    else:
        st.error("Could not retrieve fare. Please check your input values.")
else:
    st.error(f"Error: {response.status_code}")
    st.error(f"Response: {response.text}")
