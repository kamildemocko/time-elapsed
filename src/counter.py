import arrow
from humanize import precisedelta
from streamlit.delta_generator import DeltaGenerator
import streamlit as st

class Counter:
    def __init__(self, title: str, desc: str, color_hex: str, start_time: float, precise_time: bool, tz: str) -> None:
        self.title = title
        self.desc = desc
        self.color_hex = color_hex
        self.start_time = start_time
        self.precise_time = precise_time
        self.holder = self._create_holder()
        self.tz = tz
    
    def _create_holder(self) -> DeltaGenerator:
        with st.container(border=True):
            col1, col2, col3 = st.columns([0.7, 0.1, 0.2], vertical_alignment="top")

            with col1:
                st.markdown(f"### {self.title}\n{self.desc}")
                holder = st.empty()

            with col2:
                st.markdown(
                    f"""<div style="background-color:{self.color_hex}; 
                    width:30px; height: 30px; border-radius: 50%;"></div>""", 
                    unsafe_allow_html=True
                )

            with col3:
                st.button("Change date", key=self.title + "change", use_container_width=True)
                st.button("Pause timer", key=self.title + "pause", use_container_width=True)
                st.button("Delete", key=self.title + "delete", use_container_width=True)

        return holder
    
    def update(self) -> None:
        now = arrow.now(self.tz)
        time_delta = now - arrow.get(self.start_time)
        if self.precise_time:
            self.holder.text(precisedelta(time_delta, minimum_unit="seconds", format="%.0f"))
        else:
            self.holder.text(precisedelta(time_delta, minimum_unit="days", format="%.0f"))
