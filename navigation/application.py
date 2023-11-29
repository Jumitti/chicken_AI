import pickle
import random
import time

import streamlit as st

from streamlit_searchbox import st_searchbox
from chickenAI import chickenAI


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
    user_input = st.text_area("Enter your subject here:", height=200,
                              placeholder=' Impact of Artificial Intelligence on the Evolution of Medical Technologies')
    if user_input:
        button = False
    else:
        button = True

    bibliography_file = st.file_uploader("Upload Bibliography References (CSV from ZOTERO ONLY)", type=["csv"],
                                         help="Zotero only ! Open Zotero, right click on your folder, export as .csv ")
    if not bibliography_file:
        bibliography_file = None

    st.subheader("Generation Options")

    tab1, tab2, tab3 = st.columns(3, gap='large')

    with tab1:
        max_figures = st.slider("Number of figures", min_value=0, max_value=10, value=3)

        max_words = st.slider("Number of words", min_value=1000, max_value=10000, value=2000, step=250)

    with tab3:
        include_plots = st.checkbox("Include Plots")
        if include_plots:
            plot = True
        else:
            plot = False

        include_equations = st.checkbox("Include Equations")
        if include_equations:
            equation = True
        else:
            equation = False

        generation_mode = st.radio("Generation Mode", ["Strict", "Creative"],
                                   help='Strict: fit all your requests\n\nCreative: more freedom')

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
        if not citation_style:
            citation_style = 'Cell Research'

    if st.button("Hatch the Text 🐣", use_container_width=True, disabled=button):
        with st.status("Hatching... 🐣", expanded=True) as status:
            incubator = []

            understanding = chickenAI(user_input, biblio=bibliography_file).understanding_chicken()

            analysing = chickenAI(understanding).analysing_chicken()

            style = chickenAI(analysing,
                              style=writing_style,
                              modulation=generation_mode).style_chicken()

            words = chickenAI(style,
                              figures=str(max_figures),
                              words=max_words,
                              plot=include_plots,
                              equation=include_equations).words_chicken()

            biblio = chickenAI(words,
                               citation=citation_style,
                               biblio=bibliography_file).biblio_chicken()

            citation = chickenAI(biblio,
                                 citation=citation_style,
                                 biblio=bibliography_file).citation_chicken()

            refining = chickenAI(citation,
                                 max_figures,
                                 max_words,
                                 writing_style,
                                 citation_style,
                                 generation_mode,
                                 include_plots,
                                 include_equations,
                                 bibliography_file).refining_chicken()

            incubator.append([understanding, analysing, style, words, citation, refining])

            golden_chicken = chickenAI.hatching(incubator)

            status.update(label="HATCHING ! 🐔", state="complete", expanded=False)

        st.link_button("Download your ChickenAI generation 🐔", golden_chicken)

        st.balloons()
