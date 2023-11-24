import hydralit_components as hc
import streamlit as st
import streamlit_analytics
from streamlit_modal import Modal
import streamlit_lottie
import time
import json

from utils.components import footer_style, footer
from navigation.home import home_page
from navigation.application import application_page
import os


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


st.set_page_config(
    page_title='ChickenAI',
    page_icon="utils/chicken.png",
    initial_sidebar_state="expanded"
)

if 'lottie' not in st.session_state:
    st.session_state.lottie = False

if not st.session_state.lottie:
    lottfinder = load_lottiefile("utils/ChickenAI.json")
    st.lottie(lottfinder, speed=1.3, loop=False)
    time.sleep(2)
    st.session_state.lottie = True
    st.rerun()

max_width_str = f"max-width: {75}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;

                }
        </style>
        """, unsafe_allow_html=True)

# Footer

st.markdown(footer_style, unsafe_allow_html=True)

# NavBar

HOME = 'Home'
APPLICATION = 'ChickenAI'

tabs = [
    HOME,
    APPLICATION
]

option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "🤖", 'label': APPLICATION}

]

over_theme = {'txc_inactive': 'black', 'menu_background': '#F5B7B1', 'txc_active': 'white', 'option_active': '#CD5C5C'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

if chosen_tab == HOME:
    home_page()

elif chosen_tab == APPLICATION:
    application_page()

for i in range(4):
    st.markdown('#')
st.markdown(footer, unsafe_allow_html=True)

streamlit_analytics.start_tracking()

modal = Modal(key='ChickenAI', title="Terms of Use - ChickenAI", padding=50, max_width=900)

if 'popup_closed' not in st.session_state:
    st.session_state.popup_closed = False

if not st.session_state.popup_closed:
    with modal.container():
        st.markdown(
            'Welcome to ChickenAI, where innovation meets feathers. By accessing and using this site, you agree to the following terms:')
        st.markdown('')
        st.markdown('<strong>Content Integrity</strong>: The information provided on'
                    'ChickenAI is meticulously curated to emulate genuine scientific discourse. While we strive <br>for '
                    'accuracy, this platform is designed for educational and entertainment purposes. Any correlation '
                    'with actual scientific findings is purely serendipitous.</br>', unsafe_allow_html=True)
        st.markdown(
            '<strong>Information Accuracy</strong>: We endeavor to present information with the utmost precision, but we cannot guarantee the absolute accuracy or <br>applicability of the content.'
            'Please consider ChickenAI as a thought-provoking exploration rather than an authoritative source.</br>', unsafe_allow_html=True)
        st.markdown(
            '<strong>Responsible User Conduct</strong>: Your interaction with ChickenAI is expected to be conducted responsibly. '
            ' Any misuse, unauthorized access, or <br>attempt to decipher hidden chicken-related metaphors is strictly prohibited.</br>', unsafe_allow_html=True)
        st.markdown('<strong>Data Security</strong>: We take the security of your data seriously.'
                    'All information provided is handled with utmost confidentiality.'
                    'However, in the <br>vast expanse of the digital coop, no system can be completely impervious.</br>', unsafe_allow_html=True)
        st.markdown('<strong>Limitation of Liability</strong>: We disclaim any liability for the consequences of your use of ChickenAI. '
                    'This includes, but is not limited to, direct,<br> indirect, or consequential damages. For any concerns, consult our support team.</br>', unsafe_allow_html=True)
        st.markdown('<strong>Terms Modification</strong>: We reserve the right to modify these terms without prior notice. '
                    'Your continued use of ChickenAI implies acceptance of <br>the updated terms. Check periodically for changes.</br>', unsafe_allow_html=True)
        st.markdown('')
        value = st.checkbox("By clicking, you affirm that you've reviewed and accepted these terms. Enjoy your explorations within the world of ChickenAI.")
        if value:
            close = st.button('Close')
            st.session_state.popup_closed = True

st.sidebar.image("utils/ChickenAI.png",width=500)

with st.sidebar:
    st.title("Welcome to ChickenAI!")
    st.markdown(
        "ChickenAI is an advanced platform utilizing neural networks, deep learning, and artificial intelligence, including OpenAI technology. It not only analyzes text but also generates images and diagrams based on your input. "
        "Enter your research topic, and let ChickenAI hatch profound insights and visuals, all powered by cutting-edge AI!"
    )

streamlit_analytics.stop_tracking()
views = streamlit_analytics.main.counts["total_pageviews"]
st.sidebar.markdown(f"Total connections 👨🏼‍💻: {int(views)}")