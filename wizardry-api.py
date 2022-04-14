from dataclasses import dataclass
import requests
import json
from typing import List

#using Wizard World API at https://wizard-world-api.herokuapp.com/swagger/index.html

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
    

elixir_url = 'https://wizard-world-api.herokuapp.com/Elixirs'
response = requests.get(elixir_url)
data = json.loads(response)
for key, value in data.iteritems():


elixirs = []
for row in data:
    elixir_id = row['elixir_id']
    name = row['name']
    effect = row['effect']
    side_effects = row['side_effects']
    characteristic = row['characteristics']
    time = row['time']
    difficulty = row['difficulty']
    ingredients = [Ingredient(ing_row['ingredient_id'],ing_row['name']) for ing_row in row['ingredients']] 
    ingredients = [Wizard(ing_row['ingredient_id'],ing_row['name']) for wiz_row in row['inventors']]
    elixirs.append(Elixir(elixir_id, name, effect, side_effects)
