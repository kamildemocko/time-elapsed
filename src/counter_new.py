from whenever import ZonedDateTime
import streamlit as st

class NewCounter:
    def __init__(self, tz: str) -> None:
        self._create_holder()
        self.color = "#ffffff"
        self.title = ""
        self.desc = ""
        self.date = ZonedDateTime.now(tz)
        self.tz = tz
    
    def _create_holder(self) -> None:
        with st.expander("Create new"):
            with st.container(border=True):
                col1, col2, col3 = st.columns([0.07, 0.73, 0.2], vertical_alignment="bottom")

                with col1:
                    self.color = st.color_picker("Color")

                with col2:
                    self.title = st.text_input("Title", max_chars=50)
                    self.desc = st.text_input("Description", max_chars=50)
                    self.date = st.date_input("Start date", value="today")
                
                with col3:
                    st.button("Create", key="new", use_container_width=True)
    
    def get_values(self) -> tuple[str, str, str, str]:
        return self.color, self.title, self.desc, self.date
