import streamlit as st

import tools

class Sidebarr:
    def __init__(self):
        self.timezone = None

    def set_up_sidebar(self) -> None:
        all_timezones = tools.get_timezones()
        with st.sidebar:
            self.timezone = st.selectbox(
                "Timezone", 
                all_timezones,
                index=all_timezones.index(st.session_state.user_tz),
                placeholder="Please select desired timezone",
                on_change=self._tz_change_callback
            )

    def _tz_change_callback(self) -> None:
        st.cache_data.clear()
        st.session_state.user_tz = self.timezone
        tools.save_user_state()
