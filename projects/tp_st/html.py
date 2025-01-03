import streamlit as st
import streamlit.components.v1 as components

# st.write('hola')
# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

# st.header("test html import")

HtmlFile = open("projects/tp_st/tp_st.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
# print(source_code)
components.html(source_code,width=1000, height=1200,scrolling=True)



