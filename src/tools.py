import streamlit as st
import pytz

@st.cache_data
def get_timezones() -> list[str]:
    return list(pytz.all_timezones)
