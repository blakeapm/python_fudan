"""
Helper functions for the Tarte aux Pommes project.
These little elves assist with loading and saving our precious culinary components and fetching ingredients.

Let's make our cooking adventure as smooth as a well-aged brandy!
"""

import pickle

def load_item(filepath):
    """
    Load a serialized item from a file.
    Inputs:
        filepath (str): The path to the file containing the serialized item.
    Outputs:
        item (object): The deserialized item from the file.
    """
    print(f"Fetching our beloved creation from {filepath}...")
    with open(filepath, 'rb') as file:
        item = pickle.load(file)
    print("Voilà! Successfully retrieved.")
    return item

def save_item(item, filepath):
    """
    Save an item to a file.
    Inputs:
        item (object): The item to serialize and save.
        filepath (str): The path where the item will be stored.
    Outputs:
        None, but writes the item to the specified filepath.
    """
    print(f"Saving this masterpiece to {filepath} to cherish forever.")
    with open(filepath, 'wb') as file:
        pickle.dump(item, file)
    print("Enshrined in the annals of our kitchen history!")

def get_ingredient(name, amount, unit='units'):
    """
    Retrieve an ingredient with the specified amount and unit, making every ingredient feel special.
    Inputs:
        name (str): Name of the ingredient.
        amount (float or int): Amount of the ingredient.
        unit (str): Unit of measurement for the ingredient.
    Outputs:
        ingredient (dict): A dictionary with details about the ingredient.
    """
    print(f"Gathering {amount} {unit} of {name}, each one adding its own little whisper of flavor.")
    ingredient = {'name': name, 'amount': amount, 'unit': unit}
    return ingredient