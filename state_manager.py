# state_manager.py
import streamlit as st

# state_manager.py

def init_state():
    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.info = {}
        st.session_state.conversation = []

def get_current_field():
    info_fields = [
        "name",
        "email",
        "phone",
        "location",
        "experience",
        "position",
        "tech_stack"
    ]
    return info_fields[st.session_state.step]

def update_info(key, value):
    st.session_state.info[key] = value

def next_step():
    st.session_state.step += 1

def is_last_step():
    info_fields = [
        "name",
        "email",
        "phone",
        "location",
        "experience",
        "position",
        "tech_stack"
    ]
    return st.session_state.step >= len(info_fields) - 1

def reset_state():
    st.session_state.step = 0
    st.session_state.info = {}
    st.session_state.conversation = []