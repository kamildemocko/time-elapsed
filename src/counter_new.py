from datetime import time, datetime
from zoneinfo import ZoneInfo

from whenever import ZonedDateTime
import streamlit as st
from streamlit.elements.widgets.time_widgets import DateWidgetReturn

class NewCounter:
    def __init__(self, tz: str) -> None:
        self.color = "#ffffff"
        self.title = ""
        self.desc = ""
        self.date: DateWidgetReturn = None
        self.time = time(0, 0, 0)
        self.tz = tz

        self._create_holder()
    
    def _create_holder(self) -> None:
        with st.expander("Create new"):
            with st.container(border=True):
                self.title = st.text_input("Title", max_chars=50)
                self.desc = st.text_input("Description", max_chars=50)
                st.checkbox("Precise time")

                col1, col2, col3 = st.columns([0.73, 0.07, 0.2], vertical_alignment="bottom")

                with col1:
                    col_date, col_time = st.columns(2)
                    self.date = col_date.date_input("Start date", value="today")
                    self.time = col_time.time_input("Start time", value="now")

                with col2:
                    self.color = st.color_picker("Color", value=self.color)
                
                with col3:
                    st.button("Create", key="new", use_container_width=True, on_click=self._create_handle)
    
    def _create_handle(self) -> None:
        naive_dt = datetime.combine(self.date, self.time)
        aware_dt = naive_dt.replace(tzinfo=ZoneInfo(self.tz))
        dt = ZonedDateTime.from_py_datetime(aware_dt)

        print(self.color, self.title, self.desc, dt)
        # TODO: save new values to db and reload app data
