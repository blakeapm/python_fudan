"""
Script to bake the Tarte aux Pommes.
Bakes the assembled tarte to golden perfection.

Inputs:
  - assembled_tarte: the assembled tarte, ready for baking

Outputs:
  - baked_tarte: our beautiful baked tarte aux pommes!
"""

from helpers import load_item, save_item
from tools import Oven

def bake_tarte(assembled_tarte):
    """Bake until golden and glorious, my friends! The aromas alone will enchant you."""
    oven = Oven()
    baked_tarte = oven.bake(assembled_tarte, temperature='375°F', duration='30 minutes')
    save_item(baked_tarte, 'baked_tarte.pkl')

assembled_tarte = load_item('../data/serialized_data/assembled_tarte.pkl')
bake_tarte(assembled_tarte)
