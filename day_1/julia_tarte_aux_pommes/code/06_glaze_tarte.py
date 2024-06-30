"""
Script to apply an apricot glaze to the baked Tarte aux Pommes.
Adds a glossy finish to the baked tarte, enhancing both flavor and appearance.

Inputs:
  - baked_tarte: The baked tarte.
  - apricot_glaze: Prepared apricot glaze, warm and ready to brush.

Outputs:
  - glazed_tarte.pkl: the glazed tarte, stored as glazed_tarte.pkl
"""

from tools import Glazer
from helpers import load_item, save_item

def glaze_tarte(baked_tarte, apricot_glaze):
    """Let’s dress it up with a glaze as glossy as a sunlit Seine. Oh, what a finale!"""
    glazer = Glazer()
    glazed_tarte = glazer.apply(baked_tarte, apricot_glaze)
    save_item(glazed_tarte, '../data/serialized_data/glazed_tarte.pkl')

baked_tarte = load_item('../data/serialized_data/baked_tarte.pkl')
apricot_glaze = load_item('../data/serialized_data/apricot_glaze.pkl')

glaze_tarte(baked_tarte, apricot_glaze)
