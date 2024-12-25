import streamlit as st

from tools import get_timezones

class Sidebarr:
    def __init__(self):
        self.timezone = None

    def set_up_sidebar(self) -> None:
        all_timezones = get_timezones()
        with st.sidebar:
            self.timezone = st.selectbox(
                "Timezone", 
                all_timezones,
                index=all_timezones.index(st.session_state.user_tz),
                placeholder="Please select desired timezone",
            )
            st.button("Confirm", on_click=self._tz_change_callback)

    def _tz_change_callback(self) -> None:
        st.session_state.user_tz = self.timezone
