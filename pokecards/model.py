import random

import pokebase as pb


class PokemonNotFoundError(Exception):
    ...


class Pokemon:
    def __init__(self, name: str):
        self.name = name.lower()

        # API calls
        self.pkmn = pb.pokemon(self.name)
        if not hasattr(self.pkmn, "id"):
            raise PokemonNotFoundError(f"'{self.name}' could not be found")
        self.species = pb.pokemon_species(self.name)

        # extrication & normalization
        flavors = self.species.flavor_text_entries
        flavors_en = [fl.flavor_text for fl in flavors if fl.language.name == "en"]
        # look into choosing generation from remaining flavor texts
        self.flavor = random.choice(flavors_en).replace("\n", " ")
