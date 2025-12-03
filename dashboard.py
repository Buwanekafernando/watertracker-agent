import streamlit as st
import pandas as pd
from src.agent import WaterIntakeAgent, calculate_bmi, calculate_ideal_weight
from src.database import log_intake, get_intake_history

# Page Config
st.set_page_config(page_title="AI Water Tracker", page_icon="💧", layout="wide")

# Initialize Agent
if "agent" not in st.session_state:
    st.session_state.agent = WaterIntakeAgent()

agent = st.session_state.agent

# Session State for Tracker
if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# --- Welcome Screen ---
if not st.session_state.tracker_started:
    st.markdown("""
    <style>
    .big-font { font-size:50px !important; font-weight: bold; color: #00a8e8; }
    .sub-font { font-size:20px !important; color: #555; }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('<p class="big-font">AI Water Tracker 💧</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-font">Your personal AI-powered hydration companion.</p>', unsafe_allow_html=True)
        st.write("Track your intake, get smart insights, and stay healthy.")
        st.write("")
        if st.button("Start Tracking", type="primary"):
            st.session_state.tracker_started = True
            st.rerun()
    with col2:
        # Using a placeholder image that fits the theme
        st.image("https://img.freepik.com/free-vector/glass-water-concept-illustration_114360-834.jpg?w=740", width=400)

# --- Main Dashboard ---
else:
    # Sidebar: User Profile
    with st.sidebar:
        st.header("👤 User Profile")
        user_id = st.text_input("User ID", placeholder="e.g., user123")
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        weight_kg = st.number_input("Weight (kg)", min_value=1, value=70)
        height_cm = st.number_input("Height (cm)", min_value=1, value=170)
        
        st.markdown("---")
        st.markdown("### Health Stats")
        if height_cm and weight_kg:
            bmi, category = calculate_bmi(weight_kg, height_cm)
            min_ideal, max_ideal = calculate_ideal_weight(height_cm)
            st.metric("BMI", f"{bmi}", category)
            st.caption(f"Ideal Weight: {min_ideal} - {max_ideal} kg")
            
            # BMI Progress
            st.write("BMI Status:")
            if bmi < 18.5:
                st.progress(0.2, text="Underweight")
            elif 18.5 <= bmi < 24.9:
                st.progress(0.5, text="Normal")
            elif 25 <= bmi < 29.9:
                st.progress(0.8, text="Overweight")
            else:
                st.progress(1.0, text="Obese")

    # Main Content
    st.title("💧 Hydration Dashboard")
    
    # Top Metrics Row
    m1, m2, m3 = st.columns(3)
    
    # Calculate total intake for today (Basic logic)
    today_intake = 0
    if user_id:
        history = get_intake_history(user_id)
        if history:
            df_hist = pd.DataFrame(history, columns=["Intake (ml)", "Date"])
            # Assuming Date format is "%Y-%m-%d %H:%M:%S"
            df_hist["Date"] = pd.to_datetime(df_hist["Date"])
            # Filter for today
            today = pd.Timestamp.now().normalize()
            today_mask = df_hist["Date"].dt.normalize() == today
            today_intake = df_hist[today_mask]["Intake (ml)"].sum()

    with m1:
        st.metric("Daily Goal", "2500 ml", "Target") # Static goal for now
    with m2:
        delta = today_intake - 2500
        st.metric("Today's Intake", f"{today_intake} ml", f"{delta} ml")
    with m3:
        # Streak logic would need more DB work, using placeholder
        st.metric("Current Streak", "1 Day", "🔥")

    st.markdown("---")

    # Intake Input Section
    col_input, col_feedback = st.columns([1, 2])
    
    with col_input:
        st.subheader(" Water Intake")
        intake_ml = st.number_input("Amount (ml)", min_value=0, step=50, value=250)
        if st.button("Add Water", type="primary", use_container_width=True):
            if user_id and intake_ml > 0:
                log_intake(user_id, intake_ml)
                with st.spinner("AI is analyzing your hydration..."):
                    feedback = agent.analyze_intake(intake_ml, age, weight_kg, height_cm)
                    st.session_state.last_feedback = feedback
                st.success(f"Added {intake_ml}ml!")
                st.rerun() # Rerun to update metrics
            else:
                st.warning("Please enter User ID and Amount.")

    with col_feedback:
        st.subheader("AI Suggestion")
        if "last_feedback" in st.session_state:
            st.info(st.session_state.last_feedback)
        else:
            st.markdown(
                """
                <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
                    <h4>Waiting for input...</h4>
                    <p>Log your water intake to receive personalized feedback, benefits, and a drinking schedule.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

    st.markdown("---")

    # History & Charts
    st.subheader("📈 Hydration History")
    if user_id:
        history = get_intake_history(user_id)
        if history:
            df = pd.DataFrame(history, columns=["Intake (ml)", "Date"])
            df["Date"] = pd.to_datetime(df["Date"])
            
            tab1, tab2 = st.tabs(["📊 Chart", "📋 Data"])
            with tab1:
                st.bar_chart(df, x="Date", y="Intake (ml)", color="#00a8e8")
            with tab2:
                st.dataframe(df, use_container_width=True)
        else:
            st.info("No history found. Start drinking water!")
    else:
        st.warning("Enter User ID to view history.")