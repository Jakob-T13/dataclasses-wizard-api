from dataclasses import dataclass
from typing import List
import json
import requests

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
    
wizardlst = []

try:
    wizards_req = requests.get("https://wizard-world-api.herokuapp.com/wizards/")
except:
    print("could not connect to API")
    exit(1)
    
wizards_json = wizards_req.json()

for i in wizards_json:
    new_wizard = Wizard(i["id"],i["firstName"],i["lastName"])
    wizardlst.append(new_wizard)
    
print("Wizards:")
for i in wizardlst:
    print(f"{i.last_name}, {i.first_name}")
    
spell_lst = []

try:
    spell_req = requests.get("https://wizard-world-api.herokuapp.com/spells/")
except:
    print("could not connect to API")
    exit(1)

spells_json = spell_req.json()

for i in spells_json:
    new_spell = Spell(i["id"],i["name"],i["incantation"],i["effect"],i["canBeVerbal"],i["type"],i["light"],i["creator"])
    spell_lst.append(new_spell)
    
print("\nSpells:")
for i in spell_lst:
    print(f"{i.name}: {i.effect}")