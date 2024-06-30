"""
Script to generate visual figures of the Tarte aux Pommes components.
This delightful escapade involves setting a stage where each component of our Tarte aux Pommes
shines under its own spotlight. We'll decorate and capture the beauty of the pastry, applesauce,
and the final glazed tarte in a Julia-approved tableau.
"""

from helpers import load_item
from people import Decorator, Julia
from tools import Camera

def generate_figure(component, name_of_scene, decoration_style, julia_pose):
    """
    Arrange a culinary creation and capture it in its best light.
    Inputs:
        component (object): The culinary component to be photographed.
        name_of_scene (str): The filename for saving the image.
        decoration_style (str): The style in which the table is decorated.
        julia_pose (str): How Julia should pose in the scene.
    Outputs:
        Saves an image of the component at "../figures/{name_of_scene}.png".
    """

    # Create decorator instance to arrange our dish
    decorator = Decorator()

    # Setting the table
    decorator.arrange_table(decoration_style)  # Decorate the table in the specified style.

    # Julia enters the scene
    julia = Julia(dress='chef outfit', pose=julia_pose)
    julia.enter_stage()

    # Position the component
    decorator.place_on_table(component, position='center', decoration=decoration_style)

    # Camera time!
    camera = Camera()
    camera.capture(f"../figures/{name_of_scene}.png", component)

# Load components from serialized data
prepared_pastry = load_item('../data/serialized_data/prepared_pastry.pkl')
applesauce = load_item('../data/serialized_data/applesauce.pkl')
glazed_tarte = load_item('../data/serialized_data/glazed_tarte.pkl')

# Generate images for each component
generate_figure(prepared_pastry, 'pastry_preparation', 'minimalist', 'explaining')
generate_figure(applesauce, 'apples_preparation', 'rustic charm', 'smiling')
generate_figure(glazed_tarte, 'final_tarte', 'glamorous', 'proudly presenting')
