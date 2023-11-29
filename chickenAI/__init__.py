from chickenAI.eggs import eggs
from chickenAI.hatch import hatch
import streamlit as pl
import time as t
import random as r
import json
import os


class chickenAI:

    def __init__(self,
                 text,
                 figures=None,
                 words=None,
                 style=None,
                 citation=None,
                 modulation=None,
                 plot=None,
                 equation=None,
                 biblio=None):
        self.text = text if text else None
        self.figures = figures if figures else None
        self.words = words if words else None
        self.style = style if style else None
        self.citation = citation if citation else None
        self.modulation = modulation if modulation else None
        self.plot = True if plot is True else False
        self.equation = True if equation is True else False
        self.biblio = biblio if biblio else None

    def understanding_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Chicken Scrubbing...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def analysing_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Egg-samination...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def style_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Cluck-tastic Style Chooser...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def words_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Feathered Fancy Writery...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def biblio_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Bibliochick Integration...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def citation_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Cite-a-lot Chicken...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    def refining_chicken(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Plume Polishing")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

    @staticmethod
    def hatching(incubator):
        nugget = eggs.nuggets("Hatching")
        pl.write("Hatching...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

        golden_chicken = hatch.compil_hatch()

        return golden_chicken



