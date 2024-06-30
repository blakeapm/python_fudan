"""
Script to prepare pastry dough for Tarte aux Pommes.
Creates a flaky, buttery base, essential for any good French tart.

Inputs:
  - flour: all-purpose flour.
  - butter: chilled butter.
  - ice_water: ice-cold water.

Outputs:
  - prepared pastry dough, stored as 'prepared_pastry.pkl'
"""

from helpers import get_ingredient
from tools import Mixer, RollingPin, Refrigerator

def prepare_pastry(flour, butter, ice_water):
    """Prepare the pastry dough with enthusiasm and precision."""
    print("Let's master the art of pastry! Remember, nothing is too challenging with the right attitude.")
    mixer = Mixer(keep_cold=True)
    rolling_pin = RollingPin()
    dough = mixer.combine(flour, butter)
    dough = mixer.add_water(ice_water)
    rolled_dough = rolling_pin.roll(dough, thickness='3/8 inch')
    fridge = Refrigerator()
    save_item(rolled_dough, 'prepared_pastry.pkl')
    fridge.chill(rolled_dough, duration='2 hours')

flour = get_ingredient('all-purpose flour', amount=1.5, unit='cup')
butter = get_ingredient('butter', amount=1, unit='stick', temperature='chilled')
ice_water = get_ingredient('ice water', amount=float(1/3), unit='cup')

prepare_pastry(flour, butter, ice_water)
