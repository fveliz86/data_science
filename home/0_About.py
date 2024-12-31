import streamlit as st


text_cast="""
Soy sociólogo egresado de la Universidad de Buenos Aires (UBA).
Actualmente finalizando la Maestría en Explotación de Datos y Descubrimiento del Conocimiento, también en la Universidad de Buenos Aires.
Tengo experiencia en modelos predictivos (machine learning), de tipo churn, fraude, y otras variantes de modelos para la industria financiera/bancaria. Con conocimiento y experiencia en sistemas de información geográfica, series temporales y sistemas de recomendación.
Me interesa particularmente aplicar la ciencia de datos al cruce entre la sociología y la economía.
"""
text_ing="""

I’m a sociologist graduated from the University of Buenos Aires (UBA).
Currently finishing a Master of Data Science at UBA.
I’ve experience in predictive modelling (machine learning), in particular in churn, fraud, and other types of models for the financial/banking industry. I’ve also experience and knowledge in geographical information systems, temporal series and recommender systems.
I’m specially interested in applying data science to the crossover of sociology and economics.
"""

st.title('Sobre mí / About me')

cols = st.columns(2,vertical_alignment="center")

cols[0].image('home/imagen2.png', use_container_width =True)
cols[1].write(text_cast + text_ing)

pdfFileObj = open('home/Veliz, Fernando - CV (Eng).pdf', 'rb')
st.download_button('Download CV',pdfFileObj,file_name='Veliz, Fernando - CV (Eng).pdf',mime='pdf')







