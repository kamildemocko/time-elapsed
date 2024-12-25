import time

from whenever import ZonedDateTime
from tzlocal import get_localzone_name
import streamlit as st

from counter import Counter
from sidebar import Sidebarr

TIMEZONE = "Europe/Bratislava"


def main():
    print("main rerun")

    if "user_tz" not in st.session_state:
        st.session_state.user_tz = get_localzone_name()

    Sidebarr().set_up_sidebar()

    st.title("Counters")

    counters = set()

    time1 = ZonedDateTime.from_timestamp(1735148070, tz=st.session_state.user_tz)
    counter1 = Counter("Counter1", "short description", "#f0f030", time1, st.session_state.user_tz)
    counters.add(counter1)
    time2 = ZonedDateTime(2024, 12, 1, 0, 0, 0, tz=st.session_state.user_tz)
    counter2 = Counter("Counter2", "short description another", "#f0f030", time2, st.session_state.user_tz)
    counters.add(counter2)

    while True:
        _ = [counter.update() for counter in counters]

        time.sleep(1)


if __name__ == "__main__":
    main()
