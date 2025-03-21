import time

import arrow
from tzlocal import get_localzone_name
import streamlit as st

from counter_new import NewCounter
from counter import Counter
from sidebar import Sidebarr

import tools


def main():
    tools.load_user_state()

    if "user_tz" not in st.session_state:
        st.session_state.user_tz = get_localzone_name()

    Sidebarr().set_up_sidebar()

    st.title("Counters")

    new_counter = NewCounter(st.session_state.user_tz)

    counters = set()

    time1 = arrow.get(1735148070).to(st.session_state.user_tz)
    counter1 = Counter("Counter1", "short description", "#f0f030", time1.timestamp(), True, st.session_state.user_tz)
    counters.add(counter1)

    time2 = arrow.get(2025, 2, 1, 0, 0, 0).to(st.session_state.user_tz)
    counter2 = Counter("Counter2", "short description another", "#f0f030", time2.timestamp(), False, st.session_state.user_tz)
    counters.add(counter2)

    while True:
        _ = [counter.update() for counter in counters]

        time.sleep(1)


if __name__ == "__main__":
    main()
