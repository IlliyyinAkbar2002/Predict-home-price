import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
import joblib
# from sklearn import datasets
# from sklearn.ensemble import RandomForestRegressor

st.write("""
# Aplikasi Prediksi untuk Website Housing Market di Amerika

Aplikasi untuk memprediksi **Harga Rumah di Amerika**!
""")
st.write('---')

# Load the pre-trained model
model = joblib.load('linear_regression_model.sav')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Masukkan Parameter')

def user_input_features():
    type = st.sidebar.selectbox("Tipe Properti", ('Single Family Residential', 'Multi-Family (2-4 Unit)',
       'Condo/Co-op', 'Mobile/Manufactured Home',
       'Multi-Family (5+ Unit)', 'Townhouse', 'Timeshare', 'Vacant Land'))
    type_dict = dict(zip(('Single Family Residential', 'Multi-Family (2-4 Unit)', 'Condo/Co-op', 'Mobile/Manufactured Home',
       'Multi-Family (5+ Unit)', 'Townhouse', 'Timeshare', 'Vacant Land'), [4, 2, 0, 1, 3, 6, 5, 7]))
    state = st.sidebar.selectbox("Provinsi", (
        'NM', 'VA', 'AK', 'IL', 'CA', 'MD', 'LA', 'OR', 'AL', 'FL', 'ID',
       'MA', 'NY', 'VT', 'AZ'
    ))
    state_dict = dict(zip(('NM', 'VA', 'AK', 'IL', 'CA', 'MD', 'LA', 'OR', 'AL', 'FL', 'ID',
       'MA', 'NY', 'VT', 'AZ'), [10, 13, 0, 6, 3, 9, 7, 12, 1, 4, 5, 8, 11, 14, 2]))
    beds = st.sidebar.number_input("Jumlah kamar tidur", 1, 200)
    baths = st.sidebar.number_input("Jumlah kamar mandi", 1, 375)
    sqfeet = st.sidebar.number_input("Luas Tanah", 1, 112500)
    lotsize = st.sidebar.number_input("Luas Parkir", 1, 189921600)
    year = st.sidebar.number_input("Tahun dibangun", 1790, 2024)
    market = st.sidebar.number_input("Lama Publikasi (hari)", 1, 5250)
    price_sq = st.sidebar.number_input("Harga per Luas Tanah", 1, 19140)
    data = {'PROPERTY TYPE': type_dict[type],
            'BEDS': beds,
            'BATHS': baths,
            'SQUARE FEET': sqfeet,
            'LOT SIZE': lotsize,
            'YEAR BUILT': year,
            'DAYS ON MARKET': market,
            '$/SQUARE FEET': price_sq,
            'State_new': state_dict[state]}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Parameter yang diinputkan')
st.write(df)
st.write('---')

# Apply Pre-Trained Model to Make Prediction
prediction = model.predict(df)

st.header('Prediksi Harga')
st.write(prediction)
# st.write('---')

# # Explaining the model's predictions using SHAP values
# # https://github.com/slundberg/shap
# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X)

# st.header('Feature Importance')
# plt.title('Feature importance based on SHAP values')
# shap.summary_plot(shap_values, X)
# st.pyplot(bbox_inches='tight')
# st.write('---')

# plt.title('Feature importance based on SHAP values (Bar)')
# shap.summary_plot(shap_values, X, plot_type="bar")
# st.pyplot(bbox_inches='tight')