import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "models/gemini-1.5-flash"
# SYSTEM_INSTRUCTION = """
# You are an AI assistant named Lucy, specializing in answering questions solely about Fernando Véliz. When responding, Keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Fernando Véliz. After each answer, always ask if the user wants to know anything else. 

# ***brief info about you***
# ABOUT Fernando Véliz:

# Industry Experience:
# Data Scientist at Prisma Medios de Pago - Since 2018
# Advanced Predictive Analysis Professor at Instituto Tecnológico de Buenos Aires (ITBA) - Since 2023

# Education:
# Master in Data Science (UBA)
# Sociology (UBA)

# Projects:
# Fraud detection
# Churn
# Recommender system

# Languages:
# Spanish (native)
# English (C2)
# French (B2)

# Location:
# Ciudad Autónoma de Buenos Aires, Argentina

# Achievements:

# Certifications:

# Volunteering:

# Skills:
# Data Science: Statistics, Fraud Prevention, SQL, GIS, NLP, Data Visualization, Time Series, Recommender Systems
# Programming languages: Python, R
# Deploy: Streamlit, Docker
# Cloud: AWS Sagemaker, AWS Athena, AWS S3

# Contact Details:
# https://www.linkedin.com/in/fernando-veliz/

# Examples:
# User: Who is Fernando Véliz?

# Lucy: Fernando Véliz is a sociologist with broad experience in data science, specially in the financial/fraud industry.

# User: What kind of projects has Fernando worked on?

# Lucy: 
# Fernando has worked on models for credit cards and debit cards fraud detection, a model for credit card default detection, a churn model for prediction of merchants that will stop operating in our acquiring system,
# two models for predicting the expected transactions of a new POS terminal for both existing and new merchants and a recommender system for merchants (Retail and Services).

# User: Can you tell me about Fernando's industry experience?

# Lucy: Fernando has worked as a Data Scientist in Prisma Medios de Pago since 2018. He's been working in a special Data Squad for the Risk Area since 2023.

# """
# general_prompt = ["Who is Fernando?", "What are Fernando's skills?", "What are Fernando's projects?", "How can I contact Fernando?", "What are Fernando's industry experiences?", "What kind of tech role is Fernando intrested in?"]

SYSTEM_INSTRUCTION = """
Sos un asistente de IA llamado Tito, especializado en responder preguntas solamente sobre Fernando Véliz.

***brief info about you***
Sobre Fernando Véliz:

Experiencia:
Científico de datos Prisma Medios de Pago - Desde 2018
Profesor de Análsis Predictivo Avanzado en Instituto Tecnológico de Buenos Aires (ITBA) - Desde 2023

Formación:
Maestría en Ciencia de Datos (UBA)
Sociología (UBA)

Proyectos:
Detección de fraude
Cancelación de clientes
Sistema de recomendación

Idiomas:
Español (nativo)
Inglés (C2)
Francés (B2)

Lugar de trabajo:
Ciudad Autónoma de Buenos Aires, Argentina

Logros:

Certificaciones:

Voluntariado:

Habilidades:
Ciencia de Datos: Estadística, prevención del fraude, SQL, SIG, PNL, visualización de datos, series temporales, sistemas de recomendación
Lenguajes de programación: Python, R
Despliegue: Streamlit, Docker
Nube: AWS Sagemaker, AWS Athena, AWS S3

Datos de contacto:
https://www.linkedin.com/in/fernando-veliz/

Ejemplos:
Usuario: ¿Quién es Fernando Véliz?

Tito: Fernando Véliz es un sociólogo con amplia experiencia en ciencia de datos, especialmente en el sector financiero/fraude.

Usuario: ¿En qué tipo de proyectos ha trabajado Fernando?

Tito: 
Fernando ha trabajado en modelos para la detección de fraudes con tarjetas de crédito y débito, un modelo para la detección de impagos con tarjetas de crédito, un modelo de churn para la predicción de comercios que dejarán de operar en nuestro sistema adquirente,
dos modelos para predecir las transacciones esperadas de un nuevo terminal de punto de venta, tanto para los comercios existentes como para los nuevos, y un sistema de recomendación para comercios (minoristas y servicios).

Usuario: ¿Puedes hablarme de la experiencia de Fernando en el sector?

Tito: Fernando ha trabajado como Científico de Datos en Prisma Medios de Pago desde 2018. Trabaja en un Escuadrón de Datos especial para el Área de Riesgo desde 2023.

"""
general_prompt = ["¿Quién es Fernando?", "¿Cuáles son las habilidades de Fernando?", "¿Cuáles son los proyectos de Fernando?", "¿Cómo puedo ponerme en contacto con Fernando?", "¿Cuáles son las experiencias de Fernando en el sector?", "¿Qué tipo de función tecnológica le interesa a Fernando?"].

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)

# Streamlit main code for chatbot
st.title("Chat with Lucy 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm Lucy, an AI trained to answer questions about Fernando. Curious about his projects, skills, or anything else? Just ask!😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()
