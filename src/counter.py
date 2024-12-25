from whenever import ZonedDateTime
from humanize import precisedelta
from streamlit.delta_generator import DeltaGenerator
import streamlit as st

class Counter:
    def __init__(self, title: str, desc: str, color_hex: str, start_time: ZonedDateTime, tz: str) -> None:
        self.title = title
        self.desc = desc
        self.color_hex = color_hex
        self.start_time = start_time
        self.holder = self._create_holder()
        self.tz = tz
    
    def _create_holder(self) -> DeltaGenerator:
        with st.container(border=True):
            col1, col2, col3 = st.columns([0.07, 0.73, 0.2], vertical_alignment="center")

            with col1:
                st.markdown(
                    f"""<div style="background-color:{self.color_hex}; 
                    width:40px; height: 40px; border-radius: 50%;"></div>""", 
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(f"### {self.title}\n{self.desc}")
                holder = st.empty()
            
            with col3:
                st.button("Change date", key=self.title + "change", use_container_width=True)
                st.button("Delete", key=self.title + "delete", use_container_width=True)

        return holder
    
    def update(self) -> None:
        now = ZonedDateTime.now(self.tz)
        time_delta = now.difference(self.start_time).py_timedelta()
        self.holder.text(precisedelta(time_delta, minimum_unit="seconds", format="%.0f"))
