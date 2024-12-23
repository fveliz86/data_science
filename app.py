import streamlit as st

# Define the pages
profile = st.Page(
    "home/0_Sobre_mi.py",
    title="Sobre mi",
    icon=":material/description:",
    default=True,
)
copilot = st.Page(
    "projects/1_Copilot_Resumenes.py",
    title="Copilot Generación de Resúmenes",
    icon=":material/precision_manufacturing:",
)
chatbot = st.Page(
    "projects/2_Chatbot_Q&A.py",
    title="Chatbot de Preguntas y Respuestas",
    icon=":material/smart_toy:",
)

# Define the navigation panel
pg = st.navigation(
    {
        "Home": [profile],
        "Proyectos": [copilot, chatbot],
    }
)

# Start the app
pg.run()