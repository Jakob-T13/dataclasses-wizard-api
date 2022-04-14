from dataclasses import dataclass
import requests
import json
from typing import List

#using Wizard World API at https://wizard-world-api.herokuapp.com/swagger/index.html

# DEFINING DATA CLASSES
@dataclass
class Wizard:
    wizard_id: str
    first_name: str
    last_name: str

@dataclass
class Ingredient:
    ingredient_id: str
    name: str

@dataclass
class Elixir:
    elixir_id: str
    name: str
    effect: str
    side_effects: str
    characteristics: str
    time: str
    difficulty: str
    ingredients: List[Ingredient]
    inventors: List[Wizard]
    manufacturer: str

@dataclass
class House:
    house_id: str
    name: str
    house_colours: str
    founder: str
    animal: str
    element: str
    ghost: str
    common_room: str
    heads: List[Wizard]
    
    
@dataclass
class Spell:
    spell_id: str
    name: str
    incantation: str
    effect: str
    can_be_verbal: bool
    spell_type: str
    light: str
    creator: str
    

# PULLING RAW JSON FROM THE URL AND CREATING A JSON OBJECT FROM IT
elixir_url = 'https://wizard-world-api.herokuapp.com/Elixirs'
response = requests.get(elixir_url) # response is a raw json string
data = response.json() # data is a list of json objects - similar to a list of dictionaries

# ITERATING THROUGH LIST OF JSON OBJECTS
# EACH ROW IS A JSON OBJECT
elixirs = [] # after loop will be populated with Elixir objects
for row in data:
    
    # creating a variable for each key in a given json object 
    # mapping each of these to a variable in the corresponding elixir object
    elixir_id = row['id']
    name = row['name']
    effect = row['effect']
    side_effects = row['sideEffects']
    characteristic = row['characteristics']
    time = row['time']
    difficulty = row['difficulty']
    manufacturer = row['manufacturer']

    # BUILDING LISTS OF OBJECTS INSIDE OF AN OBJECT
    # ingredients and inventors are both lists of ingredient objects and wizard objects
    # respectively, so we need to create an object for every value in list of the
    # json and store it in a list within the Elixir object

    # ingredients = [Ingredient(ing_row['id'],ing_row['name']) for ing_row in row['ingredients']] 
    ingredients = []
    for ing_row in row['ingredients']:
        ingredients.append(Ingredient(ing_row['id'], ing_row['name']))

    # inventors = [Wizard(wiz_row['id'], wiz_row['firstName'], wiz_row['lastName']) for wiz_row in row['inventors']]
    inventors = []
    for wiz_row in row['inventors']:
        inventors.append(Wizard(wiz_row['id'], wiz_row['firstName'], wiz_row['lastName']))
   
    # BUILDING ELIXIR OBJECT WITH ALL THE VARIABLES DEFINED ABOVE AND APPENDING IT TO THE LIST
    elixirs.append(Elixir(elixir_id, name, effect, side_effects, characteristic, time, difficulty, ingredients, inventors, manufacturer))

print(elixirs)

# the number of variables associated with an elixir object makes this look intimidating but objects
# with less variables will look a lot cleaner, the nested variables also add complexity that could 
# be confusing.

# printing out the json initially and looking at it before you try mapping it to your own object can
# also help a lot in terms of getting used to the structure that you're mapping from
