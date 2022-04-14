from dataclasses import dataclass

#using Wizard World API at https://wizard-world-api.herokuapp.com/swagger/index.html

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
class Ingredient:
    ingredient_id: str
    name: str
    
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
    
@dataclass
class Wizard:
    wizard_id: str
    first_name: str
    last_name: str
    elixirs: List[Elixir]