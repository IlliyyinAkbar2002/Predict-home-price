import streamlit as st
from PIL import Image


def home():
    import streamlit as st

    st.write("# Predict House Price")
    image = Image.open('pexels-scott-webb-1029599.jpg')
    st.image(image)


def plotting():
    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        Illustrates a predict of house price with
Streamlit.!
"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


page_names_to_funcs = {
    "Home": home,
    "Predict house": plotting,
}

demo_name = st.sidebar.selectbox("Site-bar", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
