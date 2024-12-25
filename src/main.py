import time

from whenever import ZonedDateTime, OffsetDateTime
import pytz
from tzlocal import get_localzone_name
from humanize import precisedelta
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

TIMEZONE = "Europe/Bratislava"

@st.cache_data
def get_timezones() -> list[str]:
    return pytz.all_timezones

class Counter:
    def __init__(self, title: str, desc: str, color_hex: str, start_time: ZonedDateTime) -> None:
        self.title = title
        self.desc = desc
        self.color_hex = color_hex
        self.start_time = start_time
        self.holder = self._create_holder()
    
    def _create_holder(self) -> DeltaGenerator:
        with st.container(border=True):
            col1, col2 = st.columns([0.07, 0.93])

            with col1:
                st.markdown(
                    f"""<div style="background-color:{self.color_hex}; 
                    width:40px; height: 40px; border-radius: 20%; margin-top: 6px;"></div>""", 
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(f"### {self.title}\n{self.desc}")
                holder = st.empty()

        return holder
    
    def update(self) -> None:
        now = ZonedDateTime.now(TIMEZONE)
        time_delta = now.difference(self.start_time).py_timedelta()
        self.holder.text(precisedelta(time_delta, minimum_unit="seconds", format="%.0f"))

def main():
    st.title("Counters")
    st.write(get_localzone_name())
    counters = set()

    time1 = ZonedDateTime.from_timestamp(1735148070, tz=TIMEZONE)
    counter1 = Counter("Counter1", "short description", "#f0f030", time1)
    counters.add(counter1)
    time2 = ZonedDateTime(2024, 12, 1, 0, 0, 0, tz=TIMEZONE)
    counter2 = Counter("Counter2", "short description another", "#f0f030", time2)
    counters.add(counter2)

    while True:
        _ = [counter.update() for counter in counters]

        time.sleep(1)


if __name__ == "__main__":
    main()
