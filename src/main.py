import time

from whenever import ZonedDateTime
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
    def __init__(self, title: str, desc: str, start_time: ZonedDateTime) -> None:
        self.title = title
        self.desc = desc
        self.start_time = start_time
        self.holder = self._create_holder()
    
    def _create_holder(self) -> DeltaGenerator:
        with st.container(border=True):
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

    time1 = ZonedDateTime(2021, 1, 1, 0, 0, 0, tz=TIMEZONE)
    counter1 = Counter("Counter1", "short description", time1)
    counters.add(counter1)
    time2 = ZonedDateTime(2024, 12, 1, 0, 0, 0, tz=TIMEZONE)
    counter2 = Counter("Counter2", "short description another", time2)
    counters.add(counter2)

    while True:
        _ = [counter.update() for counter in counters]

        time.sleep(1)


if __name__ == "__main__":
    main()
