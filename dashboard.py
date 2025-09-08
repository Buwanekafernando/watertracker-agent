import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

agent = WaterIntakeAgent()

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# Welcome Screen
if not st.session_state.tracker_started:
    st.title("Welcome to Ai Water Tracker")
    st.markdown("""
    Track your daily hydration with the help of AI.
    Log your water intake and get smart feedback to stay healthy effortlessly.
    """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.experimental_rerun()

#Main Dashboard
else:
    st.title("Ai Water Tracker Dashboard")

    # Intake Logging Form
    st.subheader("Log Your Water Intake")
    user_id = st.text_input("Enter your User ID")
    age = st.number_input("Enter your age", min_value=1, max_value=120)
    weight_kg = st.number_input("Enter your weight (kg)", min_value=1)
    intake_ml = st.number_input("Water Intake (ml)", min_value=0, step=100)

    if st.button("Submit Intake"):
        if user_id and intake_ml > 0 and age and weight_kg:
            log_intake(user_id, intake_ml)
            feedback = agent.analyze_intake(intake_ml, age, weight_kg)
            st.success("Intake logged successfully!")
            st.markdown(f"**AI Feedback:** {feedback}")
        else:
            st.warning("Please fill in all fields.")

    # Intake History Viewer
    st.subheader("Your Intake History")
    if user_id:
        history = get_intake_history(user_id)
        if history:
            df = pd.DataFrame(history, columns=["Intake (ml)", "Date"])
            st.dataframe(df)
        else:
            st.info("No intake history found for this user.")