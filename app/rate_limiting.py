import streamlit as st
import time

RATE_LIMIT = 1
TIME_WINDOW = 60  # seconds

def is_rate_limited():
    now = time.time()
    
    if 'request_times' not in st.session_state:
        st.session_state.request_times = []

    # Remove timestamps older than TIME_WINDOW
    st.session_state.request_times = [
        t for t in st.session_state.request_times if now - t < TIME_WINDOW
    ]

    if len(st.session_state.request_times) >= RATE_LIMIT:
        return True
    else:
        st.session_state.request_times.append(now)
        return False