import streamlit as st



st.subheader('Proyectos de Maestría')

col1,col2,col3 = st.columns(3,vertical_alignment="center")
col1.image('projects/tp_gis/portada tp gis.png')
col2.image('projects/tp_st/portada tp st.png')
col3.image('projects/tp_especialización/portada tp especilización.png')

col1,col2,col3 = st.columns(3)
pdfFileObj = open('projects/tp_gis/TP2_G4_SIG.pdf', 'rb')
col1.download_button('TP Sistemas de Información Geográfica: “Clasificación de imágenes satelitales para la detección y cuantificación de inundaciones”',pdfFileObj,file_name='TP2_G4_SIG.pdf',mime='pdf')


import streamlit.components.v1 as components
path_to_html = "projects/tp_st/tp_st.html" 

tp_st = st.Page(
    "projects/tp_st/html.py",
    title="lalala",
    icon=":material/precision_manufacturing:",
)

col2.page_link(tp_st, label="TP Series Temporales: “Ciclos de Crecimiento Económico”")
#      
# with columns[1].button:
# with col2.container:
#     st.page_link(tp_st, label="TP Series Temporales: “Ciclos de Crecimiento Económico”")
#     st.image('projects/tp_st/portada tp st.png')
    
# st.write(f"check out this [link]({path_to_html})")

pdfFileObj = open('projects/tp_especialización/Véliz, Fernando - TP Especialización v2.pdf', 'rb')
col3.download_button('TP Especialización: "Modelo Predictivo de Puntajes de Lengua y Matemática"',pdfFileObj,file_name='Véliz, Fernando - TP Especialización v2.pdf',mime='pdf')

st.subheader('Proyectos laborales')

col1,col2,col3 = st.columns(3)
video_url='https://www.youtube.com/watch?v=oOOMiPUDEME'
col1.video(video_url)
col1.caption("'Un sistema de recomendación en acción': proyecto desarrolado en Prisma Medios de Pago")

