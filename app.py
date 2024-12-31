import streamlit as st
import streamlit.components.v1 as components

# from streamlit_option_menu import option_menu

st.set_page_config(page_title='Fernando Véliz\'s portfolio',layout="wide")

# # Define the pages
# profile = st.Page(
#     "home/0_About.py",
#     title="About me",
#     icon=":material/description:",
#     default=True,
# )
# proyectos = st.Page(
#     "projects/1_Proyectos.py",
#     title="Copilot Generación de Resúmenes",
#     icon=":material/precision_manufacturing:",
# )
# # chatbot = st.Page(
# #     "projects/2_Chatbot_Q&A.py",
# #     title="Chatbot de Preguntas y Respuestas",
# #     icon=":material/smart_toy:",
# # )



# linkedin="""
# <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
# <div class="badge-base LI-profile-badge" data-locale="es_ES" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="fernando-veliz" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ar.linkedin.com/in/fernando-veliz/es?trk=profile-badge"></a></div>              
# """              
              
# with st.sidebar:
#     components.html(linkedin,height=310)
#     st.page_link(profile)
#     st.page_link(proyectos)

# # Define the navigation panel
# pg = st.navigation(
#     {
#         'lala':[profile],
#         'ss':[proyectos]
#     }
# )

# # Start the app
# pg.run()



with st.sidebar:
    choose = option_menu(
        "Fernando Véliz",
        [
            "About Me",
            "Proyectos",
            "Skills",
            "Chatbot",
        ],
        icons=[
            "person fill",
            "book half",
            "tools",
            "robot",
        ],
        default_index=0,
        # styles={
        #     "container": {"padding": "0!important", "background-color": "#0D1117"},
        #     "icon": {"color": "darkorange", "font-size": "20px"},
        #     "nav-link": {
        #         "font-size": "17px",
        #         "text-align": "left",
        #         "margin": "0px",
        #         "--hover-color": "#1F2937",
        #     },
        #     "nav-link-selected": {"background-color": "#A41117"},
        # },
    )
    # st.markdown(
    # "<div style='text-align: center;'>"
    # "<a href='https://linkedin.com/in/rishirajsharma231'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
    # "&nbsp;&nbsp;&nbsp;&nbsp;"
    # "<a href='https://github.com/Rishiraj01'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
    # "&nbsp;&nbsp;&nbsp;&nbsp;"
    # "<a href='mailto:rishirajsharma231@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
    # "</div>",
    # unsafe_allow_html=True,
# )

pages = {
    "About Me": "home/0_About.py",
    "Proyectos": "projects/1_Proyectos.py",
    "Skills": "skills/skills.py",
    "Chatbot": "chatbot/chatbot.py",
}

# Dynamically load the selected page
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())


# st.set_page_config(
#     page_title="Rishi's Portfolio",
#     page_icon="desktop_computer",
#     layout="wide",
#     initial_sidebar_state="auto",
# )
# with st.sidebar:
#     choose = option_menu(
#         "Rishi Raj Sharma",
#         [
#             "Lucy",
#             "About Me",
#             "Experience",
#             "Technical Skills",
#             "Education",
#             "Projects",
#             "Achivements",
#             "Volunteering",
#             "Blog",
#             "Contact",
#         ],
#         icons=[
#             "robot",
#             "person fill",
#             "clock history",
#             "tools",
#             "book half",
#             "clipboard",
#             "trophy fill",
#             "heart",
#             "pencil square",
#             "envelope",
#         ],
#         menu_icon="mortarboard",
#         default_index=0,
#         styles={
#             "container": {"padding": "0!important", "background-color": "#0D1117"},
#             "icon": {"color": "darkorange", "font-size": "20px"},
#             "nav-link": {
#                 "font-size": "17px",
#                 "text-align": "left",
#                 "margin": "0px",
#                 "--hover-color": "#1F2937",
#             },
#             "nav-link-selected": {"background-color": "#A41117"},
#         },
#     )
#     st.markdown(
#     "<div style='text-align: center;'>"
#     "<a href='https://linkedin.com/in/rishirajsharma231'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
#     "&nbsp;&nbsp;&nbsp;&nbsp;"
#     "<a href='https://github.com/Rishiraj01'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
#     "&nbsp;&nbsp;&nbsp;&nbsp;"
#     "<a href='mailto:rishirajsharma231@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
#     "</div>",
#     unsafe_allow_html=True,
# )

# pages = {
#     "Lucy": "_pages/home.py",
#     "About Me": "_pages/About_Me.py",
#     "Experience": "_pages/Experience.py",
#     "Technical Skills": "_pages/technical_skills.py",
#     "Education": "_pages/Education.py",
#     "Projects": "_pages/Projects.py",
#     "Achivements": "_pages/Achivements.py",
#     "Volunteering": "_pages/Volunteering.py",
#     "Blog": "_pages/Blog.py",
#     "Contact": "_pages/Contact.py",
# }

# # Dynamically load the selected page
# page_file = pages.get(choose)
# if page_file:
#     with open(page_file, encoding="utf-8") as file:
#         exec(file.read())