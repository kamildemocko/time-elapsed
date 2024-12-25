import streamlit as st
import pytz

@st.cache_data
def get_timezones() -> list[str]:
    return list(pytz.all_timezones)

def save_user_state() -> None:
    """Saves all user preferences"""
    # TODO

def load_user_state() -> None:
    """Loads all user preferences"""
    # TODO
