

# booking_app.py
import streamlit as st
#import pandas as pd
from utils.Dashboard_Operations import dashboard_operations
from utils.Dashboard import dashboard_custome_satisf
from utils.Info_Page import landing_page
from utils.addition.graphs import graph_pes
# Title of the web app
st.title('Hotel Room Booking Application')

# Get user input for check-in date
check_in_date = st.date_input("Check-in Date")

# Get user input for check-out date
check_out_date = st.date_input("Check-out Date")

# Get user input for room type
room_type = st.selectbox("Room Type", ["Single", "Double", "Suite"])

# Get user input for number of guests
num_guests = st.number_input("Number of Guests", min_value=1, max_value=10, step=1)

# Display the selected booking details
st.write("Booking Details:")
st.write(f"Check-in Date: {check_in_date}")
st.write(f"Check-out Date: {check_out_date}")
st.write(f"Room Type: {room_type}")
st.write(f"Number of Guests: {num_guests}")

# You can add additional functionality here, such as processing the booking,
# integrating with a backend or database, and displaying confirmation messages.
