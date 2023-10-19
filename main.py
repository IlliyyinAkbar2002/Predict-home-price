# Add library
import streamlit as st
import pandas as pd
import numpy as np

st.title('Assignment Machine Learning')
st.header('Predict house price', divider='rainbow')

# Random data generator
df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.table(df)


