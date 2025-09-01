import streamlit as st
import pandas as pd
from datatime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history


if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

#Welcome 

if not st.session_state.tracker_started:
    st.title("Welcome to Ai Water Tracker")
    st.markdown("""
    Track your daily hydration with the help of Ai.
    log your water intake and get smart feedback and stay healthy effortlessly.
    """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun() 
else:
    #add the dashboard
    st.title("Ai Water Tracker Dashboard")
                
