from pokecards.card import display_card
from pokecards.cli import parse_args
from pokecards.model import Pokemon


def main():
    args = parse_args()
    pokemon = Pokemon(args.name)
    display_card(pokemon)
