from typing import cast
from datetime import time, datetime, date

import arrow
import streamlit as st

from db.models import DBItem

class NewCounter:
    def __init__(self, tz: str) -> None:
        self.color: str = "#ffffff"
        self.title: str = ""
        self.desc: str = ""
        self.date: date = date.today()
        self.time: time = time(0, 0, 0)
        self.precise_time: bool = False
        self.tz: str = tz

        self._create_holder()
    
    def _create_holder(self) -> None:
        with st.expander("Create new"):
            with st.container(border=True):
                self.title = st.text_input("Title", max_chars=50)
                self.desc = st.text_input("Description", max_chars=50)
                self.precise_time = st.checkbox("Precise time")

                col1, col2, col3 = st.columns([0.73, 0.07, 0.2], vertical_alignment="bottom")

                with col1:
                    col_date, col_time = st.columns(2)
                    self.date = cast(date, col_date.date_input("Start date", value="today"))
                    self.time = col_time.time_input("Start time", value="now", disabled=not self.precise_time)

                with col2:
                    self.color = st.color_picker("Color", value=self.color)
                
                with col3:
                    st.button("Create", key="new", use_container_width=True, on_click=self._create_handle)
    
    def _create_handle(self) -> None:
        if not self.title:
            st.error("Title is required")
            return

        naive_dt = datetime.combine(self.date, self.time)
        aware_dt = arrow.get(naive_dt).to(self.tz)

        item = DBItem(
            index=None,
            created=arrow.now().timestamp(),
            title=self.title,
            description=self.desc,
            datetime=aware_dt.timestamp(),
            precise_time=self.precise_time,
            color=self.color
        )

        # TODO: save new values to db and reload app data
        print(item)
