"""
Script to assemble the Tarte aux Pommes.
Lays down the applesauce and arranges apple slices in the prepared pastry shell.

Inputs:
  - pastry_shell: the prepared pastry shell.
  - applesauce: the applesauce.
  - apple_slices: freshly sliced apples.

Outputs:
  - the assembled tarte: stored as 'assembled_tarte.pkl' and ready for baking.
"""

from helpers import load_item, save_item
from tools import TartePan

def assemble_tarte(pastry_shell, applesauce, apple_slices):
    """Assembling the tarte, darling, let's arrange those apples like we're painting a masterpiece!"""
    tarte_pan = TartePan()
    tarte = tarte_pan.layer(pastry_shell, applesauce, apple_slices)
    save_item(tarte, '../data/serialized_data/assembled_tarte.pkl')

prepared_pastry = load_item('../data/serialized_data/prepared_pastry.pkl')
applesauce = load_item('../data/serialized_data/applesauce.pkl')
sliced_apples = load_item('../data/serialized_data/sliced_apples.pkl')

assemble_tarte(prepared_pastry, applesauce, sliced_apples)
