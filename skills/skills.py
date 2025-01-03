import streamlit as st

st.title('Skills')

columns = st.columns(4)
columns[0].button('Data Science')
columns[0].button('Statistics')
columns[0].button('Fraud Prevention')
columns[0].button('SQL')

columns[1].button('NLP')
columns[1].button('Data Visualization')
columns[1].button('Time Series')
columns[1].button('Recommender Systems')

columns[2].button('Python')
columns[2].button('R')
columns[2].button('Streamlit')
columns[2].button('Docker')

columns[3].button('AWS Sagemaker')
columns[3].button('AWS Athena')
columns[3].button('AWS S3')
columns[3].button('GIS')