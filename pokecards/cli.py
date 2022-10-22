import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("pokecards")
    parser.add_argument("name", metavar="pokemon_name")
    return parser.parse_args()
