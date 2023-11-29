import os
import json


class hatch:

    @staticmethod
    def compil_hatch():
        with open('chickenAI/golden_nuggets.json', 'r') as chicken_farm:
            chicken = json.load(chicken_farm)
        golden_chicken = chicken['chicken']
        return golden_chicken
