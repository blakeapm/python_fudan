"""
Script to make applesauce for the Tarte aux Pommes.
Transforms precooked apples into a thick, flavorful marmalade-like base.

Inputs:
  - precooked_apples: precooked apples, stored as 'precooked_apples.pkl'.
  - sugar: Sugar.
  - lemon_zest: Fresh zest from a lemon for a citrusy kick.
  - brandy: A splash of brandy for depth (optional).

Outputs:
  - applesauce: the applesauce, stored as 'applesauce.pkl'
"""

from helpers import load_item, save_item, get_ingredient
from tools import Mixer

def make_applesauce(precooked_apples, sugar, lemon_zest, brandy=None):
    """Craft a luscious applesauce, my dear, and let's make it with a bit of spirited flair!"""
    print("Turning these humble apples into a divine marmalade!")
    mixer = Mixer()
    applesauce = mixer.blend(precooked_apples, sugar, lemon_zest, brandy)
    save_item(applesauce, '../data/serialized_data/applesauce.pkl')

precooked_apples = load_item('../data/serialized_data/precooked_apples.pkl')
sugar = get_ingredient('sugar', amount=0.5, unit='cup')
lemon_zest = get_ingredient('lemon zest', amount=1)
brandy = get_ingredient('brandy', amount=2, unit='tbsp')

make_applesauce(precooked_apples, sugar, lemon_zest, brandy)
