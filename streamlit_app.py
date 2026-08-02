import streamlit as st
import joblib

model=joblib.load('model.pkl')
st.title('House Price Prediction')
area=st.number_input('Area (sq ft)',100,10000,1500)
bed=st.number_input('Bedrooms',1,10,3)
age=st.number_input('House Age',0,50,5)
if st.button('Predict Price'):
    pred=model.predict([[area,bed,age]])[0]
    st.success(f'Estimated Price: ₹ {pred:,.0f}')
