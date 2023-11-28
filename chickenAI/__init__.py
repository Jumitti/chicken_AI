from chickenAI.eggs import eggs
import streamlit as pl
import time as t
import random as r
import json
import os


class chickenAI:

    def __init__(self, text):
        self.text = text

    def understanding(self):
        nugget = eggs.nuggets(self.text)
        pl.write("Chicken Scrubbing...")
        progress_bar = pl.progress(0.0)
        for i in range(int(nugget)):
            t.sleep(r.uniform(0.75, 2))
            progress_bar.progress((i + 1) / int(nugget))

