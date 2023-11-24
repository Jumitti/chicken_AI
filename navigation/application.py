import pickle
import random
import time

import streamlit as st

from streamlit_searchbox import st_searchbox


@st.cache_resource
def csl_pickle():
    with open('utils/csl.pkl', 'rb') as file:
        return pickle.load(file)


def CSL(search_citation):
    citations_returns = []
    csl = csl_pickle()

    filtered_citations = [citation for citation in csl if search_citation.lower() in citation.lower()]

    for citation in filtered_citations:
        citations_returns.append(citation)

    return citations_returns


def application_page():
    user_input = st.text_area("Enter your subject here:", height=200, placeholder=' Impact of Artificial Intelligence on the Evolution of Medical Technologies')
    if user_input:
        button = False
    else:
        button = True

    bibliography_file = st.file_uploader("Upload Bibliography References (CSV from ZOTERO ONLY)", type=["csv"], help="Zotero only ! Open Zotero, right click on your folder, export as .csv ")

    st.subheader("Generation Options")

    tab1, tab2, tab3 = st.columns(3, gap='large')

    with tab1:
        max_figures = st.slider("Number of figures", min_value=0, max_value=10, value=3)

        max_words = st.slider("Number of words", min_value=1000, max_value=10000, value=2000, step=250)

    with tab3:
        include_plots = st.checkbox("Include Plots")

        include_equations = st.checkbox("Include Equations")

        generation_mode = st.radio("Generation Mode", ["Strict", "Creative"], help='Strict: fit all your requests\n\nCreative: more freedom')

    with tab2:
        writing_styles = [
            "Scientific",
            "Simplification",
            "Keynote",
            "Formal Academic",
            "Journalistic",
            "Narrative",
            "Persuasive",
            "Humorous",
            "Technical",
            "Literary",
            "Popular/Informal",
            "Expository",
            "Poetic"
        ]

        writing_style = st.selectbox("Writing Style", writing_styles, help='Default Scientific')

        citation_style = st_searchbox(CSL, key="Citation Style", label='Citation Style (default: Cell Research)')

    if st.button("Hatch the Text 🐣", use_container_width=True, disabled=button):

        with st.status("Hatching... 🐣", expanded=True) as status:
            '''
            random_delay = random.uniform(15, 30)
            st.write("Chicken Scrubbing...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Egg-samination...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Cluck-tastic Style Chooser...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Feathered Fancy Writery...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Bibliochick Integration...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Cite-a-lot Chicken...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Chicken Scrubbing...")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))

            random_delay = random.uniform(15, 30)
            st.write("Plume Polishing")
            progress_bar = st.progress(0.0)
            for i in range(int(random_delay)):
                time.sleep(random.uniform(0.75, 2))
                progress_bar.progress((i + 1) / int(random_delay))'''

            status.update(label="HATCHING ! 🐔", state="complete", expanded=False)

        st.link_button("Download your ChickenAI generation 🐔", 'https://r.sine.com/chicken')

        st.balloons()
