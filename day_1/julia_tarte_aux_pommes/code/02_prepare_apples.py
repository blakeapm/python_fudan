"""
Script to prepare apples for Tarte aux Pommes.
Handles the slicing and initial cooking of apples to start the base filling.

Inputs:
  - apples: Fresh apples, type and quantity.
  - lemon_juice: Amount of lemon juice for flavor and preservation.
  - sugar: Amount of sugar to enhance sweetness.

Outputs:
  - cooked apples: the prepared apples stored as 'precooked_apples.pkl'.
"""

from tools import Knife, Cooker
from helpers import get_ingredient

def prepare_apples(apples, lemon_juice, sugar):
    """Slice and pre-cook apples with a sprinkle of joy and a dash of daring!"""
    print("Diving arm-deep into apples! Here's to making it simple and making it marvelous!")
    knife = Knife()
    cooker = Cooker()
    sliced_apples = knife.slice(apples)
    precooked_apples = cooker.cook(sliced_apples, lemon_juice, sugar)
    save_item(precooked_apples, 'precooked_apples.pkl')

apples = get_ingredient('apples', amount=4)
lemon_juice = get_ingredient('lemon juice', amount=1, unit='tsp')
sugar = get_ingredient('sugar', amount=1, unit='tbsp')

prepare_apples(apples, lemon_juice, sugar)