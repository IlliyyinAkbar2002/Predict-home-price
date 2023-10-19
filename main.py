# Add library
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Assignment Machine Learning')
# Header
st.header('Predict house price', divider='rainbow')

# Sidebar
st.sidebar.header('Menu House Price')
add_selectbox = st.sidebar.selectbox(
    'How would you like to predict?',
    ('Prediction', 'Exploration')
)

# Create 3 Columns
col1, col2, col3 = st.columns(3)

# Add content
with col1:
    st.header('House Price Prediction')
    st.text('This is prediction page')

with col2:
    st.header('Image of house price', divider='rainbow')
    st.image("https://static.streamlit.io/examples/dog.jpg")
    
with col3:
    st.header('House Price Exploration')
    st.text('This is exploration page')

# Random data generator
df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.table(df)


