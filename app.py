import streamlit as st
import time
import datetime

def calculator():
    """A Streamlit calculator app with an alarm clock feature."""

    # --- Styling (Adapt to your existing style) ---
    st.markdown(
        """
        <style>
        /* Add any custom styles here to match your calculator's theme */
        .alarm-panel {
            background-color: rgba(255, 255, 255, 0.05); /* Semi-transparent white */
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            color: white; /* Adjust text color for readability */
        }
        .alarm-set {
            color: #4CAF50; /* Green for "Alarm Set" message */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Core Calculator Content ---
    st.title("⏰ Multi-Tool: Calculator & Alarm")
    st.markdown("A handy calculator with a built-in alarm clock.")

    # --- ALARM CLOCK SECTION ---
    st.header("⏰ Set an Alarm")

    with st.container():
        st.markdown("<div class='alarm-panel'>", unsafe_allow_html=True)  # Start Alarm Panel
        alarm_time = st.time_input("Set Alarm Time")
        st.markdown("</div>", unsafe_allow_html=True)  # End Alarm Panel

    if st.button("Set Alarm"):
        alarm_set = True
        st.session_state.alarm_set = True  # Store alarm status in session state
        st.success("<span class='alarm-set'>Alarm Set!</span>", unsafe_allow_html=True)  # Use styled message
        st.session_state.alarm_time = alarm_time  # Store alarm time in session state
    else:
        alarm_set = False # If alarm has not been set
        if 'alarm_set' not in st.session_state:
            st.session_state.alarm_set = False # Initialize alarm to false

    # --- Background Alarm Check (using Session State) ---
    if st.session_state.alarm_set: # Only start checking if alarm is set
        now = datetime.datetime.now().time()
        if now.hour == st.session_state.alarm_time.hour and now.minute == st.session_state.alarm_time.minute and now.second <= 5:  # Check within 5-second window
            st.balloons()
            st.warning("WAKE UP!")
            st.session_state.alarm_set = False  # Reset alarm after triggering
        else:
            time_to_alarm = datetime.datetime.combine(datetime.date.today(), st.session_state.alarm_time) - datetime.datetime.now()
            minutes = divmod(time_to_alarm.total_seconds(), 60)[0]
            if minutes > 0:
                st.info(f"Alarm will ring in {minutes:.0f} minutes") #Show the minutes left
            else:
                st.info("Alarm is set for today")



    # --- (Rest of your calculator code here) ---
    # Place the calculator functionality below the alarm clock section

    st.header("Calculator Section")  # To visually separate
    # You can now include other calculation types, as before

if __name__ == "__main__":
    calculator()
